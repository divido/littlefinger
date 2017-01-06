#!/usr/bin/env python3

from . import *

from flask import jsonify, make_response

# --------------------------------------------------------------------------------

@app.route('/create-db', methods=['POST'])
def buildDatabase():
	try:
		db.drop_all()
	except:
		pass

	db.create_all()
	return make_response("", 204)

@app.route('/accounts', methods=['GET'])
def getAccounts():
	return jsonify(accounts())

@app.route('/accounts/update', methods=['POST'])
def postUpdate():
	updateAccounts()
	return make_response("", 204)

@app.route('/entries', methods=['GET'])
def getEntries():
	return jsonify(entries())

@app.route('/types', methods=['GET'])
def getTypes():
	return jsonify(types())

@app.route('/transactions/unapproved', methods=['GET'])
def getUnapprovedTransactions():
	return jsonify(unapprovedTransactions())
