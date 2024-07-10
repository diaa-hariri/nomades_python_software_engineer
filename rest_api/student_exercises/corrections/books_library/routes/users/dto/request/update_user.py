from marshmallow import Schema, fields

class UserUpdate(Schema):
  firstname = fields.String()
  lastname = fields.String()
  username = fields.String()
  password = fields.String()
