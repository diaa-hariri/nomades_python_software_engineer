from marshmallow import Schema, fields

class BorrowingRequest(Schema):
  from_date = fields.String(required=True)
  to_date = fields.String(required=True)