#!/usr/bin/env python3

from . import db
from .table_base import TableBase, MakeParentChild
from .accounts import Account
from .types import Type

# --------------------------------------------------------------------------------

class Transaction(TableBase):
	"""A transaction represents a single logical financial movement. This is a
	virtual element, in that no banking institution sees these
	transactions. Instead, they represent collections of Entries that come
	together to form a single unit. For example, a payment to a credit card may
	represent as single transaction, but has two entries (the debit from the
	checking account and the credit to the credit card account).

	While typically a transaction will consist of one or more whole Entries, it
	is possible that a single account entry needs to be split into multiple
	transactions. For that reason, Transactions consist of EntrySubdivisions
	rather than Entries.
	"""

	_singular = 'transaction'
	_plural = 'transactions'
	__tablename__ = _plural

	name = db.Column(db.Text)
	description = db.Column(db.Text)

# --------------------

class Entry(TableBase):
	"""An entry represents a single line item on a banking statement. This is
	intended to directly reflect statements from banking institutions. These
	entries can be subdivided, then assigned to logical Transactions.
	"""

	_singular = 'entry'
	_plural = 'entries'
	__tablename__ = _plural

	# Basic Information
	transactionDate = db.Column(db.DateTime)
	type = db.Column(db.Text)
	amount = db.Column(db.Integer)
	description = db.Column(db.Text)

	# Extra Data
	checkNum = db.Column(db.Integer)
	vendorID = db.Column(db.Text)
	memo = db.Column(db.Text)

	# Categorization Data
	sic = db.Column(db.Integer) # Standard Industrial Classification
	mcc = db.Column(db.Integer) # Merchant Category Code

MakeParentChild(Account, Entry)

# --------------------

class EntrySubdivision(TableBase):
	"""This forms the glue between Entries and Transactions. Each subdivision
	references the Entry it subdivides and the Transaction it is assigned to. If
	an entry is used in whole, then a single subdivision should be created with
	a matching amount.
	"""

	_singular = 'subdivision'
	_plural = 'subdivisions'
	__tablename__ = _plural

	description = db.Column(db.Text)
	amount = db.Column(db.Integer)

MakeParentChild(Entry, EntrySubdivision)
MakeParentChild(Transaction, EntrySubdivision)
MakeParentChild(Type, EntrySubdivision)
