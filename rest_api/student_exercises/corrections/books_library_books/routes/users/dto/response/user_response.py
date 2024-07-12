from marshmallow import Schema, fields

class UserResponse(Schema):
  id = fields.String()
  username = fields.String()

class UserResponseList(Schema):
  users = fields.List(fields.Nested(UserResponse))

class UserDataResponse(Schema):
  id = fields.String()
  username = fields.String()
  firstname = fields.String()
  lastname = fields.String()