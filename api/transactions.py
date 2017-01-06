#!/usr/bin/env python3

import logging

from raw import db, Transaction

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
