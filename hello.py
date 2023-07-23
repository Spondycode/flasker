from flask import Flask, render_template


## Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
@app.route("/")
def index():
    stuff = "Whats going on here?"
    fav_pizza = ["mushroom", "Four cheeses", "Vegetarian", "Vegan", 42]
    return render_template("index.html", stuff=stuff, fav_pizza=fav_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# Create Custom Error Pages


# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# About Page
@app.route("/about")
def about():
    return render_template("about.html")
