from marshmallow import Schema, fields

class BooksUpdate(Schema):
  title = fields.String()
  authors = fields.List(fields.String())
  isbn = fields.String()