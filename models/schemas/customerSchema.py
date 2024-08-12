from . import ma
from marshmallow import fields

class CustomerSchema(ma.Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password")


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True, exclude=["password"])