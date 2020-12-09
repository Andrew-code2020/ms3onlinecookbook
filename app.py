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
    return render_template("index.html", lean_recipes=lean_recipes)


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
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "recipe_type":request.form.get("recipe_type").lower(),
            "recipe_interest": request.form.get("recipe_interest").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

    # put the new user into 'session' cookie
        session["user"] = request.form.get("first_name").lower()
        flash("Registration with Temple Lean Recipes Successful!")
        return redirect(url_for(
            "profile", first_name=session["user"]))
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"first_name": request.form.get("first_name").lower()})

        if existing_user:
            username = existing_user["first_name"]
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("first_name").lower()
                    flash(f"Welcome, {username.capitalize()}")
                    return redirect(url_for(
                        "profile", first_name=session["user"]))
            else:
                # invalid password match
                flash("Incorrect email and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<first_name>", methods=["GET", "POST"])
def profile(first_name):
    # grab the user information from mongo db and show in the user profile
    first_name = mongo.db.users.find_one(
        {"first_name": session["user"]})["first_name"]
    return render_template("profile.html", first_name=first_name)


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



#debug=false before submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

