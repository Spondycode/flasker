from flask import Flask, render_template
from jinja2.environment import TemplateStream

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


## Create a Flask Instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "my super secret key that no one knows"


# Create a Form Class
class Namerform(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    email = StringField("What's Your Email", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator
@app.route("/")
def index():
    stuff = "Whats going on here?"
    fav_pizza = ["mushroom", "Four cheeses", "Vegetarian", "Vegan", 42]
    return render_template("index.html", stuff=stuff, fav_pizza=fav_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def server_problem(e):
    return render_template("500.html"), 500


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    email = None
    form = Namerform()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        email = form.email.data
        form.email.data = ""
    return render_template("name.html", name=name, email=email, form=form)
