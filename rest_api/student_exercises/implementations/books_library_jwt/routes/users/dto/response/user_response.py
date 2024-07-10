from marshmallow import Schema, fields

class UserResponse(Schema):
  id = fields.String()
  username = fields.String()
  firstname = fields.String()

class UserResponseList(Schema):
  users = fields.List(fields.Nested(UserResponse))