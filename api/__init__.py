#!/usr/bin/env python3

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/api'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['LITTLEFINGER_DATA']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .accounts import *
from .transactions import *
