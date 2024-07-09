from flask_smorest import Blueprint
from flask.views import MethodView

from .dto.request.create_user import CreateUserRequest
from .dto.response.user_response import UserResponse, UserResponseList

from .user_service import UserService

users = Blueprint("users", "users", url_prefix="/users", description="Users operations")

user_service = UserService()

@users.route("/")
class UsersController(MethodView):
  @users.doc(description="Get all users")
  @users.response(status_code=200, schema=UserResponse(many=True), description="List of users")  
  def get(self):
    return user_service.get_all()

  
  @users.arguments(CreateUserRequest)
  @users.response(status_code=201, schema=UserResponse)
  def post(self, user: dict):
    return user_service.create_user(user)