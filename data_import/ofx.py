#!/usr/bin/env python3

import os, logging

from datetime import datetime
from ofxclient.config import OfxConfig

from raw import Account, Entry

ofxConfig = OfxConfig(file_name=os.environ['LITTLEFINGER_OFX'])
logging.info('Using OFX Config file: %s', os.environ['LITTLEFINGER_OFX'])

def importOfxAccounts(session):
	"""This adds accounts to the primary database if they are present in the OFX
	initialization file. Accounts that already exist are not updated, allowing
	the parameters to be modified independently. Accounts will be considered a
	match if the account number and ofx ID matches.
	"""

	logging.info('Importing OFX Accounts')
	for ofxAccount in ofxConfig.accounts():
		logging.debug('Processing: %s, %d', ofxAccount.institution.description, ofxAccount.number)

		try:
			account = session.query(Account).filter(
				Account.ofxID == ofxAccount.institution.client_args['id'],
			    Account.number == ofxAccount.number).one_or_none()

			if account is None:
				account = Account()
				account.name = ofxAccount.institution.description
				account.kind = 'unknown'
				account.number = ofxAccount.number
				account.ofxID = ofxAccount.institution.client_args['id']

				session.add(account)

		except Exception as e:
			logger.error(e)
			pass

def importOfxEntries(session):
	"""This downloads and imports new entries for accounts configured to use OFX
	imports. Each account is queried for a statement, then all entries are
	entered into the database. If an entry from the OFX statement matches an
	existing item in the database (matches by OFX ID, that is), then all fields
	will be updated to reflect the new statement data. Entries that are not
	included in the statement are not changed or deleted.
	"""

	accounts = session.query(Account).all();

	logging.info('Importing OFX Entries')
	for ofxAccount in ofxConfig.accounts():
		logging.debug('Processing: %s, %d', ofxAccount.institution.description, ofxAccount.number)
		try:
			account = session.query(Account).filter(
				Account.ofxID == ofxAccount.institution.client_args['id'],
			    Account.number == ofxAccount.number).one()
			statement = ofxAccount.statement(days=60)
			account.lastImport = datetime.now()

			for transaction in statement.transactions:
				entry = session.query(Entry).filter(
					Entry.account_id == Account._id,
					Entry.vendorID == transaction.id).one_or_none()

				if entry is None:
					entry = Entry()
					entry.vendorID = transaction.id
					session.add(entry)

				entry.transactionDate = transaction.date
				entry.type = transaction.type
				entry.amount = int(transaction.amount * 100)
				entry.description = transaction.payee
				entry.checkNum = transaction.checknum
				entry.memo = transaction.memo
				entry.sic = transaction.sic
				entry.mcc = transaction.mcc

				entry.account = account

		except Exception as e:
			logger.error(e)
			pass
