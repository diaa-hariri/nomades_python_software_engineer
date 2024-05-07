from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/nomades/hello')
def hello_nomades():
  return '<h1>Hello, Nomades!</h1>'

@app.route('/allow/<int:age>')
def allow_voting(age):
    return "You are allowed to enter the voting website" if age >= 18 else "You are not allowed to enter the voting website"

@app.route('/allow/<float:age>')
def allow_voting_float(age):
    return f"{age} {type(age)}"

@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/variable")
def variable():
  name = "Vincent"
  lastname = "Gaillard"
  return render_template("variable.html", name=name, lastname=lastname)

@app.route("/variable/<name>/<lastname>")
def variable_dyn(name, lastname):
  return render_template("variable.html", name=name, lastname=lastname)

@app.route("/for")
def jinja_for():
  fruits = [
    "apple",
    "banana",
    "orange",
    "watermelon",
    "peach",
    "strawberry",
    "cherry",
    "grappe"
  ]

  return render_template("for.html", fruits=fruits)

@app.route("/if")
def jinja_if():
  age = 2
  return render_template("if.html", age=age)

@app.route("/if/<int:age>")
def jinja_if_dynamic(age):
  return render_template("if.html", age=age)

@app.route("/safe")
def jinja_safe():
  html = 'antonio'
  return render_template("safe.html", html=html)

if __name__ == '__main__':
  app.run(debug=True, port=8080, host='0.0.0.0')