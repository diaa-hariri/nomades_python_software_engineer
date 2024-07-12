import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from firebase_admin import firestore

from config.database import db

class BorrowRepository:
  def __init__(self):
    self.collection = db.collection(u"borrowing")
  
  def get_all_mine(self, user_id: str) -> list[dict]:
    borrowings = []
    for borrowing in self.collection.where("user", "==", user_id).get():
      borrowing_dict = {"id": borrowing.id}
      borrowing_dict.update(borrowing.to_dict())
      borrowings.append(borrowing_dict)
    return borrowings

  def create_borrowing(self, borrowing: dict) -> dict:
    _, docRef = self.collection.add(borrowing)
    borrowing.update({"id": docRef.id})
    return borrowing
  
  def get_borrowing_by_book_id(self, book_id: str) -> list[dict]:
    # return self.collection.where("book", "==", book_id).order_by("from_date", direction=firestore.Query.DESCENDING).get()
    return self.collection.where("book", "==", book_id).get()