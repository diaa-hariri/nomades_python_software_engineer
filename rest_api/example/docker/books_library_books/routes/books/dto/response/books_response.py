from marshmallow import Schema, fields

class BooksResponse(Schema):
  id = fields.String()
  title = fields.String()
  authors = fields.List(fields.String())
  isbn = fields.String()