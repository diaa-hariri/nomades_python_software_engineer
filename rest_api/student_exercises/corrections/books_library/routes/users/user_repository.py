import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.database import db

from firebase_admin.firestore import DocumentReference, DocumentSnapshot

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
  
  def get_one(self, user_id: str) -> dict:
    docSnapshot = self.collection.document(user_id).get()
    user_dict = docSnapshot.to_dict()
    user_dict.update({"id": docSnapshot.id})
    return user_dict
  
  def update_user(self, user_id: str, updated_data: dict) -> dict:
    self.collection.document(user_id).update(updated_data)
    return self.get_one(user_id)
  
  def delete_user(self, user_id: str) -> None:
    self.collection.document(user_id).delete()
  
  def get_user_by_firstname(self, firstname: str) -> list[dict]:
    docsSnapshot: list[DocumentSnapshot] = self.collection.where("firstname", "==", firstname).get()
    docs: list[dict] = []
    for doc in docsSnapshot:
      user_dict: dict = doc.to_dict()
      user_dict.update({"id": doc.id})
      docs.append(user_dict)
    return docs