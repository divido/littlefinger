#!/usr/bin/env python3

import logging

from raw import db, Account

from data_import import importOfxAccounts, importOfxEntries

# --------------------------------------------------------------------------------

def accounts():
	"""Retrieves basic account information from the database and returns
	in. This version does not expand to include all entries.
	"""
	return [item.value for item in db.session.query(Account).all()]

# ----------------------------------------

def updateAccounts():
	"""Issues updates for all OFX accounts, downloading any new entries and
	updating any existing ones that have changed on the server.
	"""
	logging.info('Updating Accounts')

	try:
		importOfxAccounts(db.session)
		importOfxEntries(db.session)
		db.session.commit()

	except Exception as e:
		logging.error(e)
