#!/usr/bin/env python3

from eve import Eve

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

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
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///../data.sqlite',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

