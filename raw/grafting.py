#!/usr/bin/env python3

from . import db
from . import Type

# --------------------------------------------------------------------------------

def graftValue(basis, AppendClass):
	"""This takes a basis object and transforms it, replacing references to the
	specified database type with their value (from the database). It works by
	searching for foreign key references, then replacing those IDs with the
	actual values. Supplied basis is not modified; new resulting object is
	returned instead. Lists and Dictionaries are deep-copied, but other objects
	are not (their reference is copied).
	"""

	if type(basis) is list:
		return [graftValue(elem, AppendClass) for elem in basis]

	if type(basis) is dict:
		grafted = {}

		for field in basis:
			if field == AppendClass._singular + "_id":
				append = db.session.query(AppendClass).filter(AppendClass.id == basis[field]).one_or_none();
				grafted[AppendClass._singular] = None if append is None else append.value

			else:
				grafted[field] = graftValue(basis[field], AppendClass)

		return grafted

	# If not a list or dictionary, return it directly
	return basis
