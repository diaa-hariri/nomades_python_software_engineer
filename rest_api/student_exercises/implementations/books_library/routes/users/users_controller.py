from flask.views import MethodView
from flask_smorest import Blueprint

from .users_service import UserService

from .dto.request.user_create import CreateUser
from .dto.response.user_response import UserResponse

user_service = UserService()

users = Blueprint("users", "users", url_prefix="/users", description="users routes")


@users.route("/")
class UserController(MethodView):
  @users.response(status_code=200, schema=UserResponse(many=True))
  def get(self):
    return user_service.get_all()

  @users.arguments(CreateUser)
  @users.response(status_code=201, schema=UserResponse)
  def post(self, user: dict):
    return user_service.create_user(user)



@users.route("/one")
@users.response(status_code=200, schema=UserResponse)
def user_index():
  return {
    "firstname": "Antonio",
    "lastname": "Pisanello",
    "email": "antonio@nomades.ch"
  }