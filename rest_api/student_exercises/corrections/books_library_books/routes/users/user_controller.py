import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask_smorest import Blueprint
from flask import g, request
from flask.views import MethodView

from utils.decorators import authenticated

from .dto.request.create_user import CreateUserRequest
from .dto.request.update_user import UserUpdate
from .dto.response.user_response import UserResponse, UserResponseList, UserDataResponse

from .user_service import UserService

users = Blueprint("users", "users", url_prefix="/users", description="Users operations")

user_service = UserService()

@users.route("/")
class UsersController(MethodView):
  @authenticated
  @users.doc(description="Get all users")
  @users.response(status_code=200, schema=UserResponse(many=True), description="List of users")  
  @users.response(status_code=401)
  def get(self):
    """
    Returns all the users of the system
    """
    return user_service.get_all()

  
  @users.arguments(CreateUserRequest)
  @users.response(status_code=201, schema=UserResponse)
  @users.response(status_code=400)
  def post(self, user: dict):
    """"
    Insert a new user in the system

    Arguments:
      - user: dict; The user's values to insert in the system
    """
    try:
      return user_service.create_user(user), 201
    except Exception as e:
      return {"error": str(e)}
  
@users.route("/<id>")
class SpecificUserController(MethodView):
  @authenticated
  @users.response(status_code=200, schema=UserDataResponse)
  @users.response(status_code=404)
  def get(self, id: str):
    try:
      return user_service.get_one(id)
    except Exception as e:
      return {"error": str(e)}, 404

  @authenticated
  @users.arguments(UserUpdate)
  @users.response(status_code=200, schema=UserResponse)
  def put(self, update_data: dict, id: str): # /!\ Be carreful, update_data is the body sent in the request (JSON) and id is the url parameter comming from the class decorator
    return user_service.update_one(id, update_data)

  @authenticated
  @users.response(status_code=204)
  def delete(self, id:str) -> None:
    user_service.delete_user(id)

@authenticated
@users.route("/firstname/<firstname>")
@users.response(status_code=200, schema=UserResponse(many=True))
def get_user_by_firstname(firstname):
  return user_service.get_user_by_firstname(firstname)

@authenticated
@users.route("/me")
@users.response(status_code=200, schema=UserDataResponse)
def get_myself():
  return user_service.get_one(g.user_id)
