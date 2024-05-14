import random
import string
import hashlib

from .users_repository import UserRepository

class UserService:
  def __init__(self):
    self.repository = UserRepository()
  
  def get_all(self) -> list[dict]:
    return self.repository.get_all()

  def create_user(self, user_data: dict) -> dict:
    salt = "".join(random.sample(string.ascii_lowercase, 5))
    h_pwd = hashlib.sha256((salt+user_data.get("password", "")).encode("utf-8")).hexdigest()
    user_data.update({"salt": salt, "password": h_pwd})
    return self.repository.create_user(user_data)
  
