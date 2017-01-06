#!/usr/bin/env python3

import logging

from . import app
from raw import db, Transaction

from flask import jsonify
from flask.json import dumps

# --------------------------------------------------------------------------------

def unapprovedTransactions():
	"""This returns all transactions that have not been approved by the current
	user. These transactions need to be reviewed and modified, then marked as
	approved to move into the next stage of the pipelen
	"""

	unapproved = []

	transactions = db.session.query(Transaction).all()
	for transaction in transactions:
		unapproved.append(transaction.expandedValue)

	return unapproved

@app.route('/transactions/unapproved', methods=['GET'])
def getUnapprovedTransactions():
	return jsonify(unapprovedTransactions())
