from flask_smorest import Blueprint
from flask import request
from flask.views import MethodView

from .dto.request.create_user import CreateUserRequest
from .dto.request.update_user import UserUpdate
from .dto.response.user_response import UserResponse, UserResponseList

from .user_service import UserService

users = Blueprint("users", "users", url_prefix="/users", description="Users operations")

user_service = UserService()

@users.route("/")
class UsersController(MethodView):
  @users.doc(description="Get all users")
  @users.response(status_code=200, schema=UserResponse(many=True), description="List of users")  
  def get(self):
    """
    Returns all the users of the system
    """
    return user_service.get_all()

  
  @users.arguments(CreateUserRequest)
  @users.response(status_code=201, schema=UserResponse)
  def post(self, user: dict):
    """"
    Insert a new user in the system

    Arguments:
      - user: dict; The user's values to insert in the system
    """
    return user_service.create_user(user)
  
@users.route("/<id>")
class SpecificUserController(MethodView):
  @users.response(status_code=200, schema=UserResponse)
  def get(self, id: str):
    return user_service.get_one(id)

  @users.arguments(UserUpdate)
  @users.response(status_code=200, schema=UserResponse)
  def put(self, update_data: dict, id: str): # /!\ Be carreful, update_data is the body sent in the request (JSON) and id is the url parameter comming from the class decorator
    return user_service.update_one(id, update_data)

  @users.response(status_code=204)
  def delete(self, id:str) -> None:
    user_service.delete_user(id)

@users.route("/firstname/<firstname>")
@users.response(status_code=200, schema=UserResponse(many=True))
def get_user_by_firstname(firstname):
  return user_service.get_user_by_firstname(firstname)
