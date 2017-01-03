#!/usr/bin/env python3

from . import db
from .table_base import TableBase

# --------------------------------------------------------------------------------

class Type(TableBase):
	"""A Type is used to categorize expenses. Types can be any short string, and
	subtypes are created by using a dot to separate (such as
	"Health.Vitamins"). Each EntrySubdivision should contain exactly one Type to
	categorize that part of the Entry.
	"""

	_singular = 'type'
	_plural = 'types'
	__tablename__ = _plural

	name = db.Column(db.String(64))
	description = db.Column(db.Text)
