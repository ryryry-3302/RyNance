from http.client import REQUEST_TIMEOUT
import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    
    return apology("u fucked up", 400)

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    """Register user"""
    name = request.form.get("UserName")
    password = generate_password_hash(request.form.get("password"))

    if not request.form.get("username"):
        return apology("must provide username", 400)

        # Ensure password was submitted
    elif not request.form.get("password"):
        return apology("must provide password", 400)

    if request.form.get("password") != request.form.get("confirmation"):
        return apology("Passwords dont match pepega")

    if len(db.execute("SELECT username FROM users WHERE username = ?", username)) > 0:
        return apology("Username taken lol")

    db.execute('INSERT INTO users (username, hash) values(?, ?)', username, password)
    return redirect("/login")

    

    