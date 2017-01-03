#!/usr/bin/env python3

import logging

from . import app
from raw import db, Account

from data_import import importOfxAccounts, importOfxEntries

from flask import jsonify, request

# --------------------------------------------------------------------------------

def expandedAccounts(update):
	logging.info('GET /accounts, update = %s', update)

	if update:
		try:
			importOfxAccounts(db.session)
			importOfxEntries(db.session)
			db.session.commit()

		except Exception as e:
			logger.error(e)

	return {
		'accounts': [item.expandedValue for item in db.session.query(Account).all()]
	}

@app.route('/accounts', methods=['GET'])
def getAccounts():
	"""An example API GET request demonstrating direct use of raw Database
	classes and expanded values
	"""

	update = 'update' in request.args and request.args['update']
	return jsonify(expandedAccounts(update))
