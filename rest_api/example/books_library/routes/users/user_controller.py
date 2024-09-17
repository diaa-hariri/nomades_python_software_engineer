from flask.views import MethodView
from flask_smorest import Blueprint

from .user import User
from .dto.response.user_response import UserResponse, UserId
from .dto.response.user_response_list import UserResponseList

users = Blueprint("users", "users", url_prefix="/users", description="Users routes")

@users.route("/")
class UserController(MethodView):
  @users.doc(description="Retrieve a list of all the users of the system")
  @users.response(status_code=200, schema=UserResponseList(many=True), description="Return the list of all the users user")
  def get(self):
    u = User("qwertz", "Antonio", "Pisanello", "moiap13", "1234567890", "jlkshg")
    u1 = User("sdfg", "Antonio", "Pisanello", "moiap13", "1234567890", "jlkshg")
    u2 = User("ghds", "Antonio", "Pisanello", "moiap13", "1234567890", "jlkshg")
    return [
      u.to_dict(),
      u1.to_dict(),
      u2.to_dict()
    ]

  def post(self):
    return "hello from post users"
  
@users.route("/<id>")
class UserController(MethodView):
  @users.doc(description="Retrieve a specific user given the id")
  @users.response(status_code=200, schema=UserResponse, description="Return the specific user")
  def get(self, id):
    u = User("qwertz", "Antonio", "Pisanello", "moiap13", "1234567890", "jlkshg")
    u_dict = u.to_dict()
    return u_dict

  def put(self, id):
    return f"hello put users with id {id}"
  
  def delete(self, id):
    return f"hello delete users with id {id}"
