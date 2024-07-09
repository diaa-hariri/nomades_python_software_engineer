import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.database import db

class UserRepository:
  def __init__(self):
    self.collection = db.collection(u"users")

  def get_all(self) -> list[dict]:
    users = []
    for user in self.collection.get():
      user_dict = {"id": user.id}
      user_dict.update(user.to_dict())
      users.append(user_dict)
    return users
  
  def create_user(self, user: dict) -> dict:
    _, docRef = self.collection.add(user)
    user.update({"id": docRef.id})
    return user

# TODO: Create the repository function that change the user data in the database
#   - Cretae the function for getting only one user given the id
#   - Create the function for updating a specific user in the dataabse given the id
#   - Create the function for deleting a specifiy user in the database given the id