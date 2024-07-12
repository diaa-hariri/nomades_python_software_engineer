import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.google_books_api import google_books_get_by_isbn

from .books_repository import BookRepository

class BookService():
  def __init__(self):
    self.repository = BookRepository()
  
  def get_all(self) -> list[dict]:
    return self.repository.get_all()
  
  def create_book(self, book: dict) -> dict:
    if "isbn" in book:
      google_books_data = google_books_get_by_isbn(book["isbn"])
      if google_books_data is not None and "items" in google_books_data:
        google_books_data = google_books_data["items"][0]["volumeInfo"]

        if "pageCount" in google_books_data:
          book["page_count"] = google_books_data["pageCount"]
        
        if "publishedDate" in google_books_data:
          book["published_date"] = google_books_data["publishedDate"]

        if "description" in google_books_data:
          book["description"] = google_books_data["description"]
        
    return self.repository.create_book(book)