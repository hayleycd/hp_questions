from flask import Flask, request, render_template, g, redirect, url_for, flash, jsonify
from flask import session as flask_session
import os
# import models
import jinja2


# App information

app = Flask(__name__)
app.secret_key = "THISISMYPRODUCTIONANDTESTINGKEY"
app.jinja_env.undefined = jinja2.StrictUndefined


# pages

# Landing Page
@app.route("/")
def landing_page():
    """This renders the landing page."""
    return render_template("landing.html")

# Routes for setting up the database.

@app.route("/build")
def set_up_db():
    """I am setting up an interface for building the database"""
    return render_template("db.html")

@app.route("/add_category")
def add_category():
    """I am setting up an interface for building the database"""
    return render_template("add_category.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)