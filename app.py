from http.client import REQUEST_TIMEOUT
import os
import ast

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, checksalary, login_required, lookup, usd

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

uri = os.getenv("postgres://vyjjmempqhsrcy:6863da9ca9714c9629cc61f62529bf44abc3b86498c248998c3a677dd33da9a8@ec2-3-230-122-20.compute-1.amazonaws.com:5432/deh9uie1q10q4s")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)

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
    rows = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
    name = rows[0]["username"]
    records = checksalary("Computer Engineering")
    print(records)
    return render_template("index.html", name=name)

@app.route("/change", methods=["GET","POST"])
@login_required
def change():
    if request.method == "GET":
        return render_template("change.html")

    rows = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])

    if not check_password_hash(rows[0]["hash"], request.form.get("oldpassword")):
        return apology("Incorrect password", 403)
    
    if request.form.get("password") != request.form.get("confirmation"):
        return apology("Passwords dont match pepega")

    password = generate_password_hash(request.form.get("password"))
    db.execute("UPDATE users SET hash = ? WHERE id = ?", password, session["user_id"])
    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    
    email = request.form.get("inputemail")

    if not email:
            return apology("must provide username", 403)

        # Ensure password was submitted
    elif not request.form.get("password"):
        return apology("must provide password", 403)

    password = generate_password_hash(request.form.get("password"))        

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE email = ?", email)

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
        return apology("invalid username and/or password", 403)

    # Remember which user has logged in
    session["user_id"] = rows[0]["id"]

    # Redirect user to home page
    return redirect("/")
  

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
    username = request.form.get("username")
    password = generate_password_hash(request.form.get("password"))
    email = request.form.get("inputemail")

    if not request.form.get("username"):
        return apology("must provide username", 400)

        # Ensure password was submitted
    if not request.form.get("password"):
        return apology("must provide password", 400)

    if not request.form.get("inputemail"):
        return apology("must provide email", 400)    

    if request.form.get("password") != request.form.get("confirmation"):
        return apology("Passwords dont match pepega")

    if len(db.execute("SELECT email FROM users WHERE email = ?", email)) > 0:
        return apology("Email taken lol")


    db.execute('INSERT INTO users (username, hash, email) values(?, ?, ?)', username, password, email)
    if request.form.get("WantLogin") == "want":
        rows = db.execute("SELECT * FROM users WHERE email = ?", email)
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    return redirect("/login")

    
@app.route("/calculate")
@login_required
def calculate():
    return render_template("calculate.html")

@app.route("/retirement", methods=["GET", "POST"])
@login_required
def retirement():
    if request.method == "GET":
        return render_template("retirement.html")

@app.route("/learn", methods=["GET", "POST"])
@login_required
def learn():
    if request.method == "GET":
        return render_template("learn.html")


@app.route("/salary", methods=["GET", "POST"])
@login_required
def salary():
    if request.method == "GET":
        username = db.execute('SELECT username FROM users WHERE id = ?', session["user_id"])[0]['username']
        mylist = db.execute('SELECT * FROM lists WHERE username = ?', username)
        print(mylist)
        return render_template("salary.html", mylist=mylist)
    
    degree = request.form.get("degree")
    records = checksalary(degree)
    
    if records == None:
        return apology("Invalid parse")

    return render_template("salary.html", records=records, degree=degree)

@app.route("/addlist", methods=["GET", "POST"])
@login_required
def addsalary():
    if request.method == "POST":
        record = ast.literal_eval(request.form.get("addid"))
        username = db.execute('SELECT username FROM users WHERE id = ?', session["user_id"])[0]['username']
        db.execute('INSERT INTO lists (username, university, course, median, twentyfive, seventyfive, employmentrate) values(?, ?, ?, ?, ?, ?, ?)', username, record["university"], record["degree"], record["gross_monthly_median"], record["gross_mthly_25_percentile"], record["gross_mthly_75_percentile"], record["employment_rate_overall"])
        return redirect("/salary")

@app.route("/removecourse", methods=["POST"])
@login_required
def removesalary():
    if request.method == "POST":
        courseid = request.form.get("courseid")
        db.execute("DELETE FROM lists WHERE id = ?", courseid)
        return redirect("/salary")



@app.route("/budget", methods=["GET", "POST"])
@login_required
def budget():
    if request.method == "GET":
        return render_template("budget.html")