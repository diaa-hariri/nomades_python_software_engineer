from marshmallow import Schema, fields

class BorrowResponse(Schema):
  status = fields.String(required=True)
  from_date = fields.Date()
  to_date = fields.Date()

class BorrowBookResponse(BorrowResponse):
  book = fields.String(required=True)
  