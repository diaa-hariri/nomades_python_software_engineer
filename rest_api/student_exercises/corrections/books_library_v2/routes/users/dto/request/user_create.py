from marshmallow import Schema, fields

class CreateUser(Schema):
  firstname = fields.String(required=True)
  lastname = fields.String(required=True)
  username = fields.String(required=True)
  email = fields.String(required=True)
  password = fields.String(required=True)