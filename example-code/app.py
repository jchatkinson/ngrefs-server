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

@jrpc.method('App.notify')
def notify(string):
    pass

@jrpc.method('App.fails')
def fails(string):
    raise ValueError

@jrpc.method('App.getForm()')
def getForm():
    formdata = json.load(open('./forms/test.json'))
    return formdata

@jrpc.method('App.getSteelSectionProps(string) -> any')
def getSteelSectionProps(secName):
    props = {name: secName}


# Run the app
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)