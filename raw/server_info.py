#!/usr/bin/env python3

from . import db
from .table_base import TableBase

# --------------------------------------------------------------------------------

class User(TableBase):
	"""This table keeps track of user information for logging into the system.
	"""

	_singular = 'user'
	_plural = 'users'
	__tablename__ = _plural

	username = db.Column(db.Text)
	display = db.Column(db.Text)
