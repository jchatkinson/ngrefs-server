#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jeremy Atkinson http://kinson.io/
# All rights reserved.

from flask import Flask, redirect
from flask_jsonrpc import JSONRPC
import json

# Flask application
app = Flask(__name__)

# Flask-JSONRPC
jrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

# redirect baseurl '/' to the api help
@app.route('/')
def home():
    return redirect('/api/browse/')

# Sample Method
@jrpc.method('App.index')
def index():
    return u'Welcome to Flask JSON-RPC'

# More example method
@jrpc.method('App.hello')
def hello(name):
    return u'Hello {0}'.format(name)

@jrpc.method('App.helloDefaultArgs')
def hello_default_args(string='Flask JSON-RPC'):
    return u'We salute you {0}'.format(string)

@jrpc.method('App.helloDefaultArgsValidate(string=str) -> str', validate=True)
def hello_default_args_validate(string='Flask JSON-RPC'):
    return u'We salute you {0}'.format(string)

@jrpc.method('App.argsValidateJSONMode(a1=Number, a2=String, a3=Boolean, a4=Array, a5=Object) -> Object')
def args_validate_json_mode(a1, a2, a3, a4, a5):
    return u'Number: {0}, String: {1}, Boolean: {2}, Array: {3}, Object: {4}'.format(a1, a2, a3, a4, a5)

@jrpc.method('App.argsValidatePythonMode(a1=int, a2=str, a3=bool, a4=list, a5=dict) -> object')
def args_validate_python_mode(a1, a2, a3, a4, a5):
    return u'int: {0}, str: {1}, bool: {2}, list: {3}, dict: {4}'.format(a1, a2, a3, a4, a5)

@jrpc.method('App.notify')
def notify(string):
    pass

@jrpc.method('App.fails')
def fails(string):
    raise ValueError

@jrpc.method('App.sum(Number, Number) -> Number', validate=True)
def sum_(a, b):
    return a + b

@jrpc.method('App.subtract(Number, Number) -> Number', validate=True)
def subtract(a, b):
    return a - b

@jrpc.method('App.divide(Number, Number) -> Number', validate=True)
def divide(a, b):
    return a / float(b)

@jrpc.method('App.getForm()')
def getForm():
    formdata = json.load(open('./forms/test.json'))
    return formdata
    

# Run the app
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)