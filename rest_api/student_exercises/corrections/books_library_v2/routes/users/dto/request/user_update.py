from marshmallow import Schema, fields

class UpdateUser(Schema):
  firstname = fields.String()
  lastname = fields.String()
  username = fields.String()
  email = fields.String()
  password = fields.String()