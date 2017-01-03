#!/usr/bin/env python3

from . import db
from .table_base import TableBase

# --------------------------------------------------------------------------------

class Account(TableBase):
	"""This represents an account with a banking institution. These store data
	about the account, and are handled differently based on their kind. Every
	Entry references an account that it belongs to.
	"""

	_singular = 'account'
	_plural = 'accounts'
	__tablename__ = _plural

	name = db.Column(db.String(64))
	kind = db.Column(db.Enum(
		'checking',
		'savings',
		'cash',
		'credit',
		'friendly',
		'unknown'
	))

	number = db.Column(db.Integer)
	ofxID = db.Column(db.Text)
	lastImport = db.Column(db.DateTime)
