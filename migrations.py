from models import db, Contacts
from faker import Factory

from app import app 

fake = Factory.create()
# Spanish
#fake = Factory.create('es_ES')
with app.app_context():
# Reload tables
    db.drop_all()
    db.create_all()
    # Make 100 fake contacts
    for num in range(100):
        fullname = fake.name().split()
        name = fullname[0]
        surname = ' '.join(fullname[1:])
        email = fake.email()
        phone = fake.phone_number()
        # Save in database
        mi_contacto = Contacts(name, surname, email, phone)
        db.session.add(mi_contacto)
        db.session.commit()
