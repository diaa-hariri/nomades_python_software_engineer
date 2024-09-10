from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import csv
import os

CURR_DIR = os.path.dirname(__file__)

app = Flask(__name__)
# app.secret_key = "secret"
app.config["SECRET_KEY"] = "some_secret"

def authenticate(f):
  @wraps(f)
  def inner_func(*args, **kwargs):
    if not session.get("loggedin", False):
      flash("login first", "warning")
      return redirect(url_for("login"))
    
    return f(*args, **kwargs)
  return inner_func


@app.route("/")
def index():
  return render_template("index.html", active_link="a_home")

@app.route("/register", methods=["POST", "GET"])


def register():
    if request.method == "POST":
        email: str = request.form["tbxEmail"]
        pwd: str = request.form["tbxPwd"]
        uid: str = request.form["tbxUid"]
        phone: str = request.form["tbxPhone"]

        session["email"] = email
        session["pwd"] = pwd
        session["uid"] = uid
        session["phone"] = phone

        csv_file_path = f'{CURR_DIR}/users.csv'
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, pwd, uid, phone])

        flash('Successfully registered', 'success')

        return redirect(url_for("userinfo"))

    return render_template("login/register.html", active_link="a_register")




@app.route("/login", methods=["GET", "POST"])


# def login():
#   if request.method == "POST":
#     email: str = request.form["tbxEmail"]
#     pwd: str = request.form["tbxPwd"]

#     if email == "test@gmail.com" and pwd == "1234567890":
#       session["loggedin"] = True
#       session["email"] = email
#       session["pwd"] = pwd
#       flash('Login successfull', 'success')

#       return redirect(url_for("userinfo"))
#     flash('Wrong crendentials', 'danger')

#   return render_template("login/login.html", active_link="a_login")


def login():
    if request.method == "POST":
        email: str = request.form["tbxEmail"]
        pwd: str = request.form["tbxPwd"]

        csv_file_path = f'{CURR_DIR}/users.csv'
        user_found = False

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email and row[1] == pwd:
                    user_found = True
                    break
        
        if user_found:
            session["loggedin"] = True
            session["email"] = email
            session["pwd"] = pwd
            flash('Login successful', 'success')
            return redirect(url_for("userinfo"))
        else:
            flash('Wrong credentials', 'danger')

    return render_template("login/login.html", active_link="a_login")


@app.route("/logout")
@authenticate
def logout():
  session["loggedin"] = False
  return redirect(url_for("login"))

@app.route("/user/info/")
@authenticate
def userinfo():
  email: str = session.get("email", "")
  pwd: str = session.get("pwd", "")
  uid: str = session.get("uid", "")
  phone: str = session.get("phone", "")
  return render_template("userinfo.html", email=email, password=pwd, uid=uid, phone=phone, active_link="a_userinfo")

@app.route("/secret")
@authenticate
def secret():
  return "this is a secret part of the website"

if __name__ == "__main__":
  app.run(port=8080, debug=True)