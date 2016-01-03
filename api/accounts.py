#!/usr/bin/env python3

from api import app
from raw import db
from raw.tables import Account

from flask import jsonify

# --------------------------------------------------------------------------------

@app.route('/accounts', methods=['GET'])
def getAccounts():
    """An example API GET request demonstrating direct use of raw Database
    classes and more complex / custom responses than Eve
    """

    return jsonify({
        'accounts': [item.expandedValue for item in db.session.query(Account).all()]
    })
