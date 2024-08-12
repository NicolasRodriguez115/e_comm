from flask import request, jsonify
from models.schemas.customerSchema import customer_schema
from services import customerService
from marshmallow import ValidationError

def save():
    try:
        #try to validate the incoming data and deserialize
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_saved), 201 # changed from customer_data


