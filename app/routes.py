from flask import redirect, json, jsonify
from app import app, jrpc, db
from app.models import Form

@app.route('/')
@app.route('/index')
def home():
    return redirect('/api/browse/')

@jrpc.method('app.notify')
def notify(string):
    pass

@jrpc.method('app.fails')
def fails(string):
    raise ValueError

@jrpc.method('test.getForm()')
def getForm():
    formdata = Form.query.get(1)
    formdata.fields = json.loads(formdata.fields)
    return jsonify(formdata)

@jrpc.method('test.getResult() -> Number')
def getResult(a,b):
    c = a*b
    return u'c = a*b\nc = ({0})*({1})\nc = {2}'.format(a,b,c)

@jrpc.method('app.getFormNameList()')
def getFormNameList():
    names = db.session.query(Form.name).all()
    return jsonify(names)

@jrpc.method('app.getFormByName(formName=String)')
def getFormByName(formName):
    form = Form.query.filter_by(name=formName).first()
    return jsonify(form)

@jrpc.method('app.getFormById(id=int)')
def getFormById(id):
    form = Form.query.get(id)
    return jsonify(form)

@jrpc.method('app.concreteBeamFlexure(bw=Number,h=Number,d=Number,As=Number,fc=Number,fy=Number) -> Number')
def concreteBeamFlexure(bw,h,d,As,fc,fy):
    return bw*h*d*As*fc*fy
    