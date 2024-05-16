import random
import string
import hashlib

from .users_repository import UserRepository

from .user import User

class UserService:
  def __init__(self):
    self.repository = UserRepository()
  
  def get_all(self) -> list[dict]:
    return self.repository.get_all()

  def create_user(self, u: User) -> User:
    print("\n\nUser service\n\n")
    print("\n\nUserrr", type(u))
    salt = "".join(random.sample(string.ascii_lowercase, 5))
    h_pwd = hashlib.sha256((salt+u.password).encode("utf-8")).hexdigest()
    # user_data.update({"salt": salt, "password": h_pwd})
    u.password = h_pwd
    u.salt = salt
    return self.repository.create_user(u)
  
  def get_one(id: str) -> User:
    pass
  
  def delete_user_by_id(id: str) -> None:
    pass

  def update_user(u: User) -> User:
    pass
