from flask import Flask, render_template


## Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
@app.route("/")
def index():
    stuff = "Whats going on here?"
    fav_pizza = ["mushroom", "Four cheeses", "Vegeetarian", "Vegan"]
    return render_template("index.html", stuff=stuff, fav_pizza=fav_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
