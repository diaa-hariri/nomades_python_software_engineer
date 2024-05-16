from marshmallow import Schema, fields

class CreateBook(Schema):
  isbn = fields.String()
  title = fields.String()
  authors = fields.List(fields.String())