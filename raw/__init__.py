#!/usr/bin/env python3

import os

from eve import Eve

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from flask import make_response

from .table_base import DOMAIN, Base

from .server_info import *
from .accounts import *
from .types import *
from .transactions import *
from .commentary import *

# --------------------------------------------------------------------------------

app = Eve(__name__, validator=ValidatorSQL, data=SQL, settings={
    'DOMAIN': DOMAIN,
    'RESOURCE_METHODS': ['GET', 'POST'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'APPLICATION_ROOT': '/raw',
    'SQLALCHEMY_DATABASE_URI': os.environ['LITTLEFINGER_DATA'],
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

@app.route('/create-db', methods=['GET'])
def buildDatabase():
	try:
		db.drop_all()
	except:
		pass

	db.create_all()
	return make_response("", 204)
