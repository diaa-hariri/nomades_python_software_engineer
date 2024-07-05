from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
import csv
from utils.decorators import authenticated
import hashlib
import random
import string

CURR_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
def register():
  if "loggedin" in session and session["loggedin"]:
    return redirect(url_for("userinfo"))
  
  if request.method == "POST":
    email = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of the input
    pwd = request.form["tbxPwd"]

    if email == "" or "@" not in email or pwd == "":
      flash("Email password must be sets", "danger")
      return redirect(url_for("register"))

    csv_file = f"{CURR_DIR}/users.csv"
    with open(csv_file, "r") as f:
      reader = csv.reader(f)
      next(reader)
      rows = list(reader)
      try:
        session_id = int(rows[-1][-1])+1
      except:
        session_id = 1

      for row in rows:
        if email == row[0]:
          flash("Email or password not valid", "danger")
          return redirect(url_for("register")) 


    with open(csv_file, "a") as f:
      fieldnames = ["email", "password", "salt", "uid"]
      writer = csv.DictWriter(f, fieldnames)
      salt = "".join([random.choices(string.ascii_letters)[0] for _ in range(10)])
      h_pwd = hashlib.sha256((pwd + salt).encode()).hexdigest()

      writer.writerow({
        "email": email,
        "password": h_pwd,
        "salt": salt,
        "uid": session_id,
      })

      session["email"] = email
      session["password"] = pwd
      session["uid"] = session_id
      session["loggedin"] = True
      
      return redirect(url_for("userinfo"))
  return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  if "loggedin" in session and session["loggedin"]:
    return redirect(url_for("userinfo"))
  
  if request.method == "POST":
    email = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of the input
    pwd = request.form["tbxPwd"]

    if email == "" or "@" not in email or pwd == "":
      flash("Email password must be sets", "danger")
      return redirect(url_for("register"))
    

    csv_file = f"{CURR_DIR}/users.csv"
    with open(csv_file, "r") as f:
      reader = csv.reader(f)
      next(reader)
      for row in reader:
        h_pwd = hashlib.sha256((pwd+row[2]).encode()).hexdigest()
        if email == row[0] and h_pwd == row[1]:
          flash("Login successful", "success")

          session["email"] = email
          session["password"] = pwd
          session["uid"] = row[-1]
          session["loggedin"] = True

          return redirect(url_for("userinfo"))
  
      flash("Email/Password doens't match", "danger")
  return render_template("login.html")

@app.route("/logout")
@authenticated
def logout():
  session.clear()
  return redirect(url_for("login"))

@app.route("/user/info")
@authenticated
def userinfo():
  email = session["email"]
  password = session["password"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, passwod=password, uid=uid)

@app.route("/secret")
@authenticated
def secret():  
  return "secret part" 

if __name__ == "__main__":
  app.run(debug=True, port=8080)