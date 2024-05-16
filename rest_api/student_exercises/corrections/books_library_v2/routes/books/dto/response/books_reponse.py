from marshmallow import Schema, fields

class BookResponse(Schema):
  isbn = fields.String(required=True)
  title = fields.String()
  authors = fields.List(fields.String())

class BookFullResponse(BookResponse):
  id = fields.String(required=True)

class BooksResponse(Schema):
  books = fields.List(fields.Nested(BookResponse))