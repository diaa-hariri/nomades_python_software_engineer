import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from config.database import db

class UserRepository:
  def __init__(self):
    self.collection = db.collection(u"users")
  
  def get_all(self) -> list[dict]:
    users = []
    for user in self.collection.stream():
      udict = {"id": user.id}
      udict.update(user.to_dict())
      users.append(udict)
    return users
  
  def create_user(self, user_data: dict) -> dict:
    print("user data", user_data)
    user_email = self.collection.where("email", "==", user_data.get("email", "")).get()
    username = self.collection.where("username", "==", user_data.get("username", "")).get()

    print(len(user_email), len(username))

    if len(user_email) > 1 or len(username) > 1:
      raise Exception(f'User with email {user_data.get("email", "")} or username {user_data.get("username", "")} already exists')
    
    _, docRef = self.collection.add(user_data)
    user_data.update({"id": docRef.id})
    return user_data

  def get_user_by_id(self, id: str) -> dict:
    # TODO: get a user with a given id
    # the id is the id of the document
    pass

  def delete_user_by_id(self, id: str) -> None:
    pass

  def update_user_by_id(self, id: str) -> dict:
    pass


