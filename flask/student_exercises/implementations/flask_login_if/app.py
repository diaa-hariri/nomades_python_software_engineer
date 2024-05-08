from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret"

users = [] # or you can use a dictionary approach to store the users {}

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    # TODO: get values from the form 
    # hint: user request.form
    # then add the new registered user to the users list or dictionary
    email = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of the input
    return redirect(url_for("userinfo"))
  
  return render_template("register.html")

@app.route("/user/info")
def userinfo():
  # TODO: protect user info page
  # only logged in persons can acces to this route
  # use session to keep in memory if logged and values
  email = session["email"]
  password = session["password"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, passwod=password, uid=uid)

#TODO: create a route for login that can be accessed by GET and POST
# when acceding by get only return the login.html file
# when acceding by POST:
#  1. get the data from form
#  2. loop through the users list or dictionary and check if email/password match
#  2.1. if you want to not use the list or dictionary you can put a basic if statement to check if the email and password are the same as the hardcoded values (default values)
#  3. if there is a match put the datas in session and then redirect to userinfo

#TODO: create logout page
# logout should destroy the session
# redirect to Login

#TODO: HTML PART
# change the base file to display the login and register links only if the user is not logged in
# change the base file to display the logout link only if the user is logged in
# You should also put the href value of <a> tags to the correct routes, i.e. use url_for() ;P
# Pay attention there is a TODO in the login.html file, you should put the correct action in the form tag i.e. use url_for() ;P

if __name__ == "__main__":
  app.run(debug=True)