#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/api'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import api.accounts
