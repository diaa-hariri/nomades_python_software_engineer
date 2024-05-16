from flask.views import MethodView
from flask_smorest import Blueprint

from .users_service import UserService

from .dto.request.user_create import CreateUser
from .dto.request.user_update import UpdateUser
from .dto.response.user_response import UserResponse, UserFullResponse

from .user import User
from .user_mapper import toEntity, toUserResponse, toUpdateEntity

user_service = UserService()

users = Blueprint("users", "users", url_prefix="/users", description="users routes")

@users.route("/")
class UserController(MethodView):
  @users.response(status_code=200)
  def get(self):
    return user_service.get_all()

  @users.arguments(CreateUser)
  @users.response(status_code=201, schema=UserFullResponse)
  def post(self, user: dict):
    return user_service.create_user(toEntity(user))

@users.route("/<id>")
class SingleUserController(MethodView):
  @users.response(status_code=200, schema=UserResponse)
  def get(self, id: str):
    return user_service.get_one(id)
  
  @users.response(status_code=204)
  def delete(self, id: str):
    user_service.delete_user_by_id(id)
    return None

  @users.arguments(UpdateUser)
  @users.response(status_code=200, schema=UserResponse)
  def put(self, user: dict, id: str):
    user.update({"id": id})
    return user_service.update_user(toUpdateEntity(user))


@users.route("/one")
@users.response(status_code=200, schema=UserResponse)
def user_index():
  return {
    "firstname": "Antonio",
    "lastname": "Pisanello",
    "email": "antonio@nomades.ch"
  }