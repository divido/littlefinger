#!/usr/bin/env python3

from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime

from .table_base import TableBase, RegisterTable, MakeParentChild
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

	name = Column(String(128))
	description = Column(Text)

RegisterTable(Transaction)

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
	transactionDate = Column(DateTime)
	type = Column(Text)
	amount = Column(Integer)
	description = Column(Text)

	# Extra Data
	checkNum = Column(Integer)
	vendorID = Column(Text)
	memo = Column(Text)

	# Categorization Data
	sic = Column(Integer) # Standard Industrial Classification
	mcc = Column(Integer) # Merchant Category Code

MakeParentChild(Account, Entry)
RegisterTable(Entry)

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

	description = Column(Text)
	amount = Column(Integer)

MakeParentChild(Entry, EntrySubdivision)
MakeParentChild(Transaction, EntrySubdivision)
MakeParentChild(Type, EntrySubdivision)
RegisterTable(EntrySubdivision)
