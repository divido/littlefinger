#!/usr/bin/env python3

import logging

from raw import db, Entry

# --------------------------------------------------------------------------------

def entries():
	"""This returns all entries from the database
	"""

	return [entry.value for entry in db.session.query(Entry).all()]
