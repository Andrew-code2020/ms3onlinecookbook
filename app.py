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
@app.route("/get_recipes")
def get_recipes():
    lean_recipes = mongo.db.lean_recipes.find()
    return render_template("base.html", lean_recipes=lean_recipes)


@app.route("/home_page")
def home_page():
    lean_recipes = mongo.db.lean_recipes.find()
    return render_template("homepage.html", lean_recipes=lean_recipes)


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
    return render_template("register.html")



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
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    user = mongo.db.users.find_one({"username": session["user"]})
    if session["user"]:
        return render_template("profile.html", username=username, user=user)

    return redirect(url_for("login"))



@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/breakfast", methods=["GET", "POST"])
def breakfast():
    return render_template("breakfast.html")


@app.route("/lunch", methods=["GET", "POST"])
def lunch():
    return render_template("lunch.html")


@app.route("/dinner", methods=["GET", "POST"])
def dinner():
    return render_template("dinner.html")


@app.route("/snacks", methods=["GET", "POST"])
def snacks():
    return render_template("snacks.html")


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
    return render_template("edit_profile.html", user=user)


@app.route("/delete_profile/<user_id>")
def delete_profile(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    session.pop("user")
    flash("Profile Deleted")
    return redirect(url_for('register'))


#debug=false before submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

