#!/usr/bin/env python3

import os, logging

from datetime import datetime
from dateutil import parser
from ofxclient.config import OfxConfig

from raw import Account, Entry
from .inferencing import inferTransactionFromEntry

ofxConfig = OfxConfig(file_name=os.environ['LITTLEFINGER_OFX'])
logging.info('Using OFX Config file: %s', os.environ['LITTLEFINGER_OFX'])

def parseToDate(value):
	try:
		if isinstance(value, datetime):
			return value;

		return parser.parse(value)

	except Exception as e:
		logging.warning("Could not parse value (%s) a valid date: %s", value, e)
		return None

def parseToInt(value):
	try:
		if value is None or value == "":
			return None

		return int(value)

	except Exception as e:
		logging.warning("Could not parse value (%s) as valid integer: %s", value, e)
		return None

def importOfxAccounts(session):
	"""This adds accounts to the primary database if they are present in the OFX
	initialization file. Accounts that already exist are not updated, allowing
	the parameters to be modified independently. Accounts will be considered a
	match if the account number and ofx ID matches.
	"""

	logging.info('Importing OFX Accounts')
	for ofxAccount in ofxConfig.accounts():
		logging.debug('Processing: %s, %d', ofxAccount.institution.description, parseToInt(ofxAccount.number))

		try:
			account = session.query(Account).filter(
				Account.ofxID == ofxAccount.institution.client_args['id'],
			    Account.number == parseToInt(ofxAccount.number)).one_or_none()

			if account is None:
				account = Account()
				account.name = ofxAccount.institution.description
				account.kind = 'unknown'
				account.number = parseToInt(ofxAccount.number)
				account.ofxID = ofxAccount.institution.client_args['id']

				session.add(account)

		except Exception as e:
			logging.error(e)
			pass

def importOfxEntries(session):
	"""This downloads and imports new entries for accounts configured to use OFX
	imports. Each account is queried for a statement, then all entries are
	entered into the database. If an entry from the OFX statement matches an
	existing item in the database (matches by OFX ID, that is), then all fields
	will be updated to reflect the new statement data. Entries that are not
	included in the statement are not changed or deleted.
	"""

	accounts = session.query(Account).all()

	logging.info('Importing OFX Entries')
	for ofxAccount in ofxConfig.accounts():
		logging.debug('Processing: %s, %d', ofxAccount.institution.description, parseToInt(ofxAccount.number))
		try:
			account = session.query(Account).filter(
				Account.ofxID == ofxAccount.institution.client_args['id'],
			    Account.number == parseToInt(ofxAccount.number)).one()
			statement = ofxAccount.statement(days=60)
			account.lastImport = datetime.now()

			for ofxEntry in statement.transactions:
				if ofxEntry.amount == 0:
					# Skip processing on $0 entries. These aren't real statement
					# entries, anyway.
					continue

				entry = session.query(Entry).filter(
					Entry.account_id == Account.id,
					Entry.vendorID == ofxEntry.id).one_or_none()

				if entry is None:
					entry = Entry()
					entry.vendorID = ofxEntry.id
					session.add(entry)

				entry.transactionDate = parseToDate(ofxEntry.date)
				entry.type = ofxEntry.type
				entry.amount = parseToInt(ofxEntry.amount * 100)
				entry.description = ofxEntry.payee
				entry.checkNum = parseToInt(ofxEntry.checknum)
				entry.memo = ofxEntry.memo
				entry.sic = parseToInt(ofxEntry.sic)
				entry.mcc = parseToInt(ofxEntry.mcc)

				entry.account = account
				inferTransactionFromEntry(session, entry)

		except Exception as e:
			logging.error(e)
			pass
