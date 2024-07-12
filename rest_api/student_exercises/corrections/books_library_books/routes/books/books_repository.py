import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.database import db

from firebase_admin.firestore import DocumentReference, DocumentSnapshot

class BookRepository:
  def __init__(self):
    self.collection = db.collection(u"books")

  def get_all(self) -> list[dict]:
    books = []
    for book in self.collection.get():
      book_dict = {"id": book.id}
      book_dict.update(book.to_dict())
      books.append(book_dict)
    return books
  
  def create_book(self, book: dict) -> dict:
    _, docRef = self.collection.add(book)
    book.update({"id": docRef.id})
    return book
  
  def get_book_by_id(self, book_id: str) -> dict:
    docSnapshot = self.collection.document(book_id).get()
    if not docSnapshot.exists:
      raise Exception(f"Book with id {book_id} doesn't exists in database")
    
    book_dict = docSnapshot.to_dict()
    book_dict.update({"id": docSnapshot.id})
    return book_dict
  