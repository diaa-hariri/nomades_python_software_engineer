import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from config.database import db

from .book import Book
from .books_mapper import to_entity, to_dict


# TODO: Create the class for managing the books collection
class BooksRepository():
  def __init__(self):
    self.collection = db.collection("books")

  def get_all(self) -> list[Book]:
    return [to_entity(book) for book in self.collection.stream()]

  def create_book(self, b: Book) -> Book:
    if b.isbn != "":
      book_isbn = self.collection.where("isbn", "==", b.isbn).get()

      if len(book_isbn) > 0:
        raise Exception("Book already exist in DB")
    
    _, docRef = self.collection.add(to_dict(b))
    return to_entity(docRef)






