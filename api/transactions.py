#!/usr/bin/env python3

import logging

from . import app
from raw import db, Entry

from flask import jsonify
from flask.json import dumps

# --------------------------------------------------------------------------------

def unassignedEntries():
	"""This returns all entries that are not fully assigned to
	transactions. This occurs when the sum of the EntrySubdivisions does not
	equal the total value of the entry.
	"""

	# Fake this routine by returning all entries for the moment...
	unassigned = []

	entries = db.session.query(Entry).all()
	for entry in entries:
		unassigned.append({
			'entry': entry.expandedValue,
			'remainingAmount': entry.amount
		})

	return unassigned

@app.route('/unassigned-entries', methods=['GET'])
def getUnassignedEntries():
	"""This endpoint wraps the unassignedEntries() method in JSON formatting
	"""

	return jsonify(unassignedEntries())
