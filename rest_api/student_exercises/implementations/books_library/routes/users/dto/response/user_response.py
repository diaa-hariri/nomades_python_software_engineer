from marshmallow import Schema, fields

class UserResponse(Schema):
  firstname = fields.String()
  email = fields.String()