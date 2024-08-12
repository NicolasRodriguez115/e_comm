from database import db
from models.customer import Customer

def save(customer_data):
    new_customer = Customer(
        name = customer_data['name'],
        email = customer_data['email'],
        password = customer_data['password'],
        phone = customer_data['phone'],
        username = customer_data['username']
    )
    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer)
    return new_customer
