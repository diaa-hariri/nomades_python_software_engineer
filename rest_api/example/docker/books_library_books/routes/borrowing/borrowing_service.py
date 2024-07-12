import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask import g
import datetime

from utils.helpers import convert_isostirng_date_to_datetime
from routes.books.books_repository import BookRepository

from .borrowing_repository import BorrowRepository

class BorrowingSeervice:
  def __init__(self):
    self.repository = BorrowRepository()
    self.book_repository = BookRepository()

  def get_all_mine(self) -> list[dict]:
    my_borrows = self.repository.get_all_mine(g.user_id)
    my_borrows_ret = []
    for borrow in my_borrows:
      borrow_book = self.book_repository.get_book_by_id(borrow["book"])
      borrow.update({"book": borrow_book["title"]})
      my_borrows_ret.append(borrow)
    
    return my_borrows_ret

  
  def create_borrowing(self, book_id: str, borrowing: dict) -> dict:
    from_date = convert_isostirng_date_to_datetime(borrowing["from_date"])

    if not self.is_book_available_for_borrow(book_id, from_date):
      raise ValueError("Book is not available for borrowing at the selected date")

    to_date = convert_isostirng_date_to_datetime(borrowing["to_date"])
    
    if from_date >= to_date:
      raise ValueError("From date must be before to date to borrow a book and you cannot borrow a book for less than 1 day")
    
    return self.repository.create_borrowing({
        "user": g.user_id, 
        "book": book_id, 
        "from_date": from_date, 
        "to_date": to_date
      })
  
  def is_book_available_for_borrow(self, book_id: str, from_date: datetime.datetime) -> bool:
    book_borrows = self.repository.get_borrowing_by_book_id(book_id)
    for borrow in book_borrows:
      borrow = borrow.to_dict()
      
      if datetime.datetime.fromtimestamp(borrow["from_date"].timestamp()) <= from_date and datetime.datetime.fromtimestamp(borrow["to_date"].timestamp()) >= from_date:
        return False
      
    return True