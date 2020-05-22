from flask import redirect
from app import app, jrpc

@app.route('/')
@app.route('/index')
def home():
    return redirect('/api/browse/')

@jrpc.method('App.notify')
def notify(string):
    pass

@jrpc.method('App.fails')
def fails(string):
    raise ValueError