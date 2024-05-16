from marshmallow import Schema, fields

class UserResponse(Schema):
  firstname = fields.String()
  email = fields.String()

class UserFullResponse(Schema):
  id = fields.String()
  firstname = fields.String()
  lastname = fields.String()
  email = fields.String()
  username = fields.String()
  password = fields.String()
  salt = fields.String()