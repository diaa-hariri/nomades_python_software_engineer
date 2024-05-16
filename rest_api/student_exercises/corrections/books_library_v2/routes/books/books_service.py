from .books_repository import BooksRepository
from .book import Book

class BooksService:
  def __init__(self):
    self.repository = BooksRepository()
  
  def get_all(self) -> list[Book]:
    return self.repository.get_all()

  def create_book(self, b: Book) -> Book:
    return self.repository.create_book(b)
