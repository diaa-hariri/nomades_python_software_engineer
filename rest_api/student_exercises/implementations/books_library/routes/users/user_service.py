import string
import hashlib
import random

from .user_repository import UserRepository

class UserService:
  def __init__(self):
    self.repository = UserRepository()

  def get_all(self) -> list[dict]:
    return self.repository.get_all()

  def create_user(self, user: dict) -> dict:
    salt = "".join(random.choices(string.ascii_letters, k=10))
    user["salt"] = salt
    user["password"] = hashlib.sha256((user["password"]+salt).encode()).hexdigest()
    return self.repository.create_user(user)
  
# TODO: create the missing function that implement the get, update and delete on a specific user
#   - ProTip: Try to specify in function signature the type you expect as parameters and the type of return of the function
