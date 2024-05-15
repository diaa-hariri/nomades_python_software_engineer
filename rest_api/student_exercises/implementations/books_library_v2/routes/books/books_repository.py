import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from config.database import db

from .book import Book


# TODO: Create the class for managing the books collection
class BooksRepository():
  def __init__():
    # TODO: create constructor and store the collections u"books" as attribute of the class
    pass

  def get_all() -> list[Book]:
    # TODO: Create the get_all() function that returns all the books of the collection
    pass

  def create_book(b: Book) -> Book:
    # TODO: Create the create_book() function that create a book in firestore database
    pass