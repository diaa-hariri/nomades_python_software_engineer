# TODO: Create the login controller
#   - Create the blueprint for the login, the url_prefix should be `/login`
#   - Create a POST route on `/login` that accepts as argument the LoginRequest DTO
#   - Call the login function from the login_service class
#   - Returns the token as a LoginResponse

from flask_smorest import Blueprint
from flask import jsonify, request

from .dto.request.login_request import LoginRequest
from .dto.response.login_response import LoginResponse

from .login_service import LoginService

login = Blueprint("login", __name__, url_prefix="/login")

login_service = LoginService()

@login.route("/", methods=["POST"])
@login.arguments(LoginRequest)
@login.response(status_code=200, schema=LoginResponse)
@login.response(status_code=401)
def login_func(login_req: dict):
  try:
    return {"token" : login_service.login(login_req)}
  except Exception as e:
    return {"error": "Wrong credentials"}, 401
