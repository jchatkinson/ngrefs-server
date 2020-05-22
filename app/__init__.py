from flask import Flask, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
app.config.from_object(Config)

jrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models