from flask import Flask, jsonify, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)