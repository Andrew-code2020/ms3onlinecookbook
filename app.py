import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
# Renders Home page
# to user or person
# browsing the web
@app.route("/home_page")
def home_page():
    lean_recipes = mongo.db.lean_recipes.find()
    return render_template("homepage.html", lean_recipes=lean_recipes)


# Allow the user to create a profile and register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_user:
            flash("email address already in use")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "recipe_type": request.form.get("recipe_type").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

    # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration with Temple Lean Recipes Successful!")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("register.html", page='register')


# Allows a registered user to log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format
                      (request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:  # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page='login')


# Allows a logged in
# user to access their
# profile and have there
# profile information
# returned to the screen
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    user = mongo.db.users.find_one({"username": session["user"]})
    if session["user"]:
        return render_template("profile.html",
                               username=username, user=user, page='profile')

    return redirect(url_for("login"))


# allows the user to log out
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# breakfast page navigation and data
@app.route("/breakfast", methods=["GET", "POST"])
def breakfast():
    breakfast_meals = mongo.db.lean_recipes.find({"recipe_types": "Breakfast"})
    print(breakfast_meals)
    return render_template("breakfast.html",
                           breakfast_meals=breakfast_meals, page='breakfast')


# lunch page navigation and data
@app.route("/lunch", methods=["GET", "POST"])
def lunch():
    lunch_meals = mongo.db.lean_recipes.find({"recipe_types": "Lunch"})
    print(lunch_meals)
    return render_template("lunch.html", lunch_meals=lunch_meals, page='lunch')


# dinner page navigation and data
@app.route("/dinner", methods=["GET", "POST"])
def dinner():
    dinner_meals = mongo.db.lean_recipes.find({"recipe_types": "Dinner"})
    print(dinner_meals)
    return render_template("dinner.html",
                           dinner_meals=dinner_meals, page='dinner')


# snack page navigation and data
@app.route("/snacks", methods=["GET", "POST"])
def snacks():
    snack_meals = mongo.db.lean_recipes.find({"recipe_types": "Snacks"})
    print(snack_meals)
    return render_template("snacks.html",
                           snack_meals=snack_meals, page='snacks')


# Allows user to recipe to Temple Lean site
@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    return render_template("add_recipe.html")


# add recipes to breakfast page
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        # check if recipe already exists in db
        existing_recipe = mongo.db.lean_recipes.find_one(
            {"meal_name": request.form.get("meal_name").lower()})
        if existing_recipe:
            flash("Recipe Name already exists")
            return redirect(url_for("breakfast"))
        add_recipe = {
            "recipe_types": request.form.get("recipe_types"),
            "recipe_image": request.form.get("recipe_image"),
            "meal_name": request.form.get("meal_name"),
            "meal_ingredients": request.form.get("meal_ingredients"),
            "meal_method": request.form.get("meal_method"),
            "meal_time": request.form.get("meal_time"),
            "meal_tools": request.form.get("meal_tools"),
            "meal_nutracarbs": request.form.get("meal_nutracarbs"),
            "meal_nutrafats": request.form.get("meal_nutrafats"),
            "meal_nutraproteins": request.form.get("meal_nutraproteins"),
            "meal_nutrakcals": request.form.get("meal_nutrakcals"),
            "created_by": session["user"],
        }
        mongo.db.lean_recipes.insert_one(add_recipe)
        flash("Recipe Created Successfully!")

    return redirect(url_for(
        "profile", username=session["user"]))


# allows the user to edit their recipes
@app.route("/editrecipe/<recipe_id>", methods=["GET", "POST"])
def editrecipe(recipe_id):
    if request.method == "POST":
        print(f"USER: {recipe_id}")
        editrec = {"$set": {
            "recipe_types": request.form.get("recipe_types"),
            "recipe_image": request.form.get("recipe_image"),
            "meal_name": request.form.get("meal_name"),
            "meal_ingredients": request.form.get("meal_ingredients"),
            "meal_method": request.form.get("meal_method"),
            "meal_time": request.form.get("meal_time"),
            "meal_tools": request.form.get("meal_tools"),
            "meal_nutracarbs": request.form.get("meal_nutracarbs"),
            "meal_nutrafats": request.form.get("meal_nutrafats"),
            "meal_nutraproteins": request.form.get("meal_nutraproteins"),
            "meal_nutrakcals": request.form.get("meal_nutrakcals"),
            "created_by": session["user"],
        }}
        mongo.db.lean_recipes.update_one({"_id": ObjectId(recipe_id)}, editrec)
        flash("Recipe updated successfully")
        return redirect(url_for(
            "profile", username=session["user"]))

    lean_recipes = mongo.db.lean_recipes.find_one({"_id": ObjectId(recipe_id)})
    types = mongo.db.types.find()
    return render_template("edit_recipe.html",
                           lean_recipes=lean_recipes, recipe_types=types)


# allows the user to edit their profile
@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if request.method == "POST":
        print(f"USER: {user_id}")
        submit = {"$set": {
            "username": request.form.get("username"),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "recipe_type": request.form.get("recipe_type"),
            "email": request.form.get("email"),
            "created_by": session["user"]
        }}
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, submit)
        flash("Profile updated successfully")

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    types = mongo.db.types.find()
    return render_template("edit_profile.html", user=user, recipe_type=types)


# Deletes user profile and logs them outá
@app.route("/delete_profile/<user_id>")
def delete_profile(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    # log out user as well
    session.pop("user")
    flash("Profile Deleted")
    return redirect(url_for('register'))


# Allows the user to delete their recipes
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.lean_recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for(
        "profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
