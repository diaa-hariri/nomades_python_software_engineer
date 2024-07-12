from marshmallow import fields
from .books_update import BooksUpdate

class BooksCreate(BooksUpdate):
  title = fields.String(required=True)
  authors = fields.List(fields.String(), required=True)