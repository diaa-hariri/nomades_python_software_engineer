# TODO: Create a class that will define the login service (logic of login)
#   - create a function login that take a dict in parameter containing username and password
#   - The login function should call the login_repository (or user_repository as you prefer) to find the user that match the same username
#   - Given the user create the password and check if it match the one sotred in database
#     - if yes -> generate the token using the `my_jwt.py` module
#     - else -> returns an error 401, with message "wrong credentials" /!\
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import hashlib

from utils.my_jwt import create_token
from routes.users.user_repository import UserRepository


class LoginService():
  def __init__(self) -> None:
    self.repository = UserRepository()

  def login(self, login_request: dict) -> str:
    user: dict = self.repository.get_user_by_username(login_request["username"])
    h_pwd = hashlib.sha256((login_request["password"]+user["salt"]).encode()).hexdigest()
    
    if h_pwd != user["password"]:
      raise Exception("Passwords don't match")
    
    return create_token(user["id"])



