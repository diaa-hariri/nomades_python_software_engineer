from flask import Flask, render_template, request, session, redirect, url_for
import json
import hashlib
import string
import random
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret"

users: list[dict] = [] # or you can use a dictionary approach to store the users {}

with open('users.json', 'r') as f:
    users = json.load(f)

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not ("loggedin" in session and session["loggedin"]):
      return redirect(url_for('login'))
    
    return func(*args, **kwargs)
  return inner

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
def register():
  if session.get("loggedin", False):
    return redirect(url_for("userinfo"))
  
  if request.method == "POST":
    # TODO: get values from the form 
    # hint: user request.form
    # then add the new registered user to the users list or dictionary
    try:
      email = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of the input
      uid = request.form["tbxUid"] # here be sure that the key of the dictionary is the NAME html attribute of the input
      pwd = request.form["tbxPwd"] # here be sure that the key of the dictionary is the NAME html attribute of the input
    except KeyError:
      return "Error, please fill all the fields", 400
    
    for user in users:
      if user["email"] == email or user["uid"] == uid:  
        return "Email / UID already used"
    
    salt = "".join(random.sample(string.ascii_lowercase, 5))
    h_pwd = hashlib.sha256((salt+pwd).encode("utf-8")).hexdigest()
    
    user = {
      "email": email,
      "uid": uid,
      "password": h_pwd,
      "salt": salt
    }

    users.append(user)

    session["loggedin"] = True
    session["email"] = email
    session["uid"] = uid
    session["password"] = pwd
    with open("users.json", "w") as j:
      j.write(json.dumps(users))
    return redirect(url_for("userinfo"))
  
  return render_template("register.html")

#TODO: create a route for login that can be accessed by GET and POST
# when acceding by get only return the login.html file
# when acceding by POST:
#  1. get the data from form
#  2. loop through the users list or dictionary and check if email/password match
#  2.1. if you want to not use the list or dictionary you can put a basic if statement to check if the email and password are the same as the hardcoded values (default values)
#  3. if there is a match put the datas in session and then redirect to userinfo
@app.route("/login", methods=["GET", "POST"])
def login():
  if session.get("loggedin", False):
    return redirect(url_for("userinfo"))
  
  if request.method == "POST":
    email = request.form.get("tbxEmail", "")
    pwd = request.form.get("tbxPwd", "")
    for user in users:
      if user["email"] == email:
        salt = user.get("salt", "")
        h_pwd = hashlib.sha256((salt+pwd).encode("utf-8")).hexdigest()
        if user["password"] == h_pwd:
          session["loggedin"] = True
          session["email"] = email
          session["uid"] = user["uid"]
          session["password"] = pwd
          return redirect(url_for("userinfo")) 
    
    return render_template("login.html") 

  return render_template("login.html")

#TODO: create logout page
# logout should destroy the session
# redirect to Login
@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for("login"))

#TODO: HTML PART
# change the base file to display the login and register links only if the user is not logged in
# change the base file to display the logout link only if the user is logged in
# You should also put the href value of <a> tags to the correct routes, i.e. use url_for() ;P
# Pay attention there is a TODO in the login.html file, you should put the correct action in the form tag i.e. use url_for() ;P

@app.route("/user/info")
@authenticated
def userinfo():
  # TODO: protect user info page
  # only logged in persons can acces to this route
  # use session to keep in memory if logged and values
  
  email = session["email"]
  password = session["password"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, password=password, uid=uid)

@app.route("/secret")
@authenticated
def secret():
  return "This is secret"

if __name__ == "__main__":
  app.run(debug=True)