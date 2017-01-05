#!/usr/bin/env python3

import os

from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy

# --------------------------------------------------------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['LITTLEFINGER_DATA']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --------------------------------------------------------------------------------

from .server_info import *
from .accounts import *
from .types import *
from .transactions import *
from .commentary import *

# --------------------------------------------------------------------------------

@app.route('/create-db', methods=['POST'])
def buildDatabase():
	try:
		db.drop_all()
	except:
		pass

	db.create_all()
	return make_response("", 204)
