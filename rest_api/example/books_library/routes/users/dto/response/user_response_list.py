from marshmallow import Schema, fields

class UserResponseList(Schema):
  id = fields.String()
  firstname = fields.String()
  lastname = fields.String()
  username = fields.String()