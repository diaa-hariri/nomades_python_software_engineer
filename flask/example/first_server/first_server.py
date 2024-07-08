from flask import Flask, jsonify, render_template, request, session, redirect, url_for, flash
from routes.login.login_wtf import wtf_login

app = Flask(__name__)
app.config["SECRET_KEY"] = "somesecret"

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route("/antonio")
def antonio():
  return "Antonio"

@app.route("/name/<user_name>")
def hello_name(user_name):
  return f"Hello {user_name}"

@app.route('/allow/<int:age>')
def allow_voting(age):
    return "You are allowed to enter the voting website" if age >= 18 else "You are not allowed to enter the voting website"

@app.route("/test/json")
def test_json():
  fruits = ["Apple", "Banana", "Watermelon", "Pear"]
  return jsonify(fruits)

@app.route("/variable")
def variable():
  p_name = "Antonio"
  p_lastname = "Pisanello"
  return render_template("variable.html", j_name=p_name, j_lastname=p_lastname)

@app.route("/variable/<p_name>/<string:p_lastname>")
def variable2(p_name,p_lastname):
 # p_name = "Antonio"
#p_lastname = "Pisanello"
  d_name = {
    "name": p_name,
    "lastname": p_lastname
  }
  return render_template("variable_dict.html", names=d_name)

@app.route("/for")
def jinja_for():
  fruits = [
    "apple",
    "banana",
    "orange",
    "watermelon",
    "peach",
    "strawberry"
  ]

  return render_template("for.html", fruits=fruits)

@app.route("/if/<int:age>")
def jinja_if(age):
  return render_template("if.html", age=age)

@app.route("/safe")
def jinja_safe():
  html = '<script>alert("Hacked!!!")</script>'
  return render_template("safe.html", html=html)

@app.route("/example/formulars")
def example_forms():
  return render_template("formulars/names.html")

@app.route("/names", methods=["POST"])
def example_names():
  print(request.form)
  firstname = request.form["uid"]
  lastname = request.form["pwd"]

  return render_template("formulars/names_render.html", firstname=firstname, lastname=lastname)

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["tbx-email"]
    pwd = request.form["tbx-pwd"]

    if email=="antonio@nomades.ch" and pwd=="1234567890":
      session["loggedin"] = True
      session["email"] = email
      flash("login successful", "success")
      return redirect(url_for("user_info"))

    flash("email/password doesnt match", "danger")
  return render_template("login/login.html")

@app.route("/logout")
def logout():
  session["loggedin"] = False
  session.pop("loggedin")
  session.clear()

  return redirect(url_for("login"))

@app.route("/userinfo")
def user_info():
  if not ("loggedin" in session and session["loggedin"]):
    return redirect(url_for("login"))
  
  return render_template("userinfo/userinfo.html", email=session["email"])

@app.route("/secret")
def secret():
  if not ("loggedin" in session and session["loggedin"]):
    return redirect(url_for("login"))
  
  return "This is a secret part of the website"

  


@app.route('/counter')
def index():
    session['count'] = session.get('count', 0) + 1
    return f'Count: {session["count"]}'



app.register_blueprint(wtf_login)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)