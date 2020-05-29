from app import db
from app.models import Form
from flask import json

form = json.load(open('./app/forms/multiply.json'))
formstring = json.dumps(form)

f = Form(name='test',
title='test form',
subtitle='a test form loaded from sqlite', 
imageUrl='./assets/test.jpg',
fields=formstring,
calcmethod='test.getResult'
)

db.session.add(f)
db.session.commit()
