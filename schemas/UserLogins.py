from marshmallow import Schema, fields

class UserLoginsSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password_hash = fields.Str(required=True)
    email = fields.Str(required=True)
    
class UpdateUserLoginsSchema(Schema):
    username = fields.Str(required=True)
    password_hash = fields.Str(required=True)
    email = fields.Str(required=True)
    
