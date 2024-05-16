# TODO: If you want ;P
from .book import Book

from firebase_admin.firestore import DocumentReference, DocumentSnapshot

def to_entity(book_data: dict | DocumentReference | DocumentSnapshot) -> Book:
  b = Book()

  if isinstance(book_data, DocumentReference):
    book_data = book_data.get()
  if isinstance(book_data, DocumentSnapshot):
    b.id = book_data.id
    book_data = book_data.to_dict()

  b.isbn = book_data["isbn"]
  b.title = book_data["title"]
  b.authors = book_data["authors"]
  return b

def to_dict(b: Book) -> dict:
  return {
    "id": b.id,
    "isbn": b.isbn,
    "title": b.title,
    "authors": b.authors,
  }