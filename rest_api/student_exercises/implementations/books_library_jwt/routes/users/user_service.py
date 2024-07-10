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
  
  def get_one(self, user_id: str) -> dict:  
    return self.repository.get_one(user_id)
  
  def update_one(self, user_id: str, updated_data: dict) -> dict:
    if "password" in updated_data:
      salt = "".join(random.choices(string.ascii_letters, k=10))
      updated_data["salt"] = salt
      updated_data["password"] = hashlib.sha256((user["password"]+salt).encode()).hexdigest() 
    
    return self.repository.update_user(user_id, updated_data)
  
  def delete_user(self, user_id: str) -> None:
    self.repository.delete_user(user_id)
  
  def get_user_by_firstname(self, firstname: str) -> list[dict]:
    return self.repository.get_user_by_firstname(firstname)