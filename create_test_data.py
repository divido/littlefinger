#!/usr/bin/env python3

from datetime import date

from raw import db
from raw import User, Account, Entry, Transaction, EntrySubdivision

db.drop_all()
db.create_all()

# --------------------------------------------------------------------------------
# Create some users

user = {
    'john': User(username='john', display='John'),
    'jane': User(username='jane', display='Jane')
}

db.session.add_all(user.values())

# --------------------------------------------------------------------------------
# Create some accounts

acct = {
    'savings': Account(name='Bank Savings',  kind='savings'),
    'check':   Account(name='Bank Checking', kind='checking'),
    'creditA': Account(name='Credit Card A', kind='credit'),
    'creditB': Account(name='Credit Card B', kind='credit'),
    'john':    Account(name='John Cash',     kind='cash'),
    'jane':    Account(name='Jane Cash',     kind='cash'),
}

db.session.add_all(acct.values())

# --------------------------------------------------------------------------------
# Create the transactions / etc.

jan1 = date(2016, 1, 1)
jan2 = date(2016, 1, 2)
jan3 = date(2016, 1, 3)
jan4 = date(2016, 1, 4)
jan5 = date(2016, 1, 5)

entry = {}
trans = {}
subd = {}

# --------------------

entry['pay'] = Entry(transactionDate=jan1, postDate=jan1, sealed=True,
                     amount=+100000, account=acct['check'],
                     description='PAYROLL DEPOSIT')

trans['pay'] = Transaction(name='Acme Paycheck', sealed=True)

subd['pay'] = EntrySubdivision(entry=entry['pay'], transaction=trans['pay'],
                               amount=+100000)

# --------------------

entry['dpt'] = Entry(transactionDate=jan1, postDate=jan2, sealed=True,
                     amount=-7500, account=acct['creditA'],
                     description='DEPARTMENT STORE')

trans['dpt'] = Transaction(name='Department Store', sealed=True,
                           description='Clothes for Winter')

subd['dpt1'] = EntrySubdivision(entry=entry['dpt'], transaction=trans['dpt'],
                                amount=-2500, description='Pants')

subd['dpt2'] = EntrySubdivision(entry=entry['dpt'], transaction=trans['dpt'],
                                amount=-5000, description='Sweaters')

# --------------------

entry['grc'] = Entry(transactionDate=jan2, postDate=jan2, sealed=True,
                     amount=-12045, account=acct['creditB'],
                     description='SUPERMARKET')

trans['grc'] = Transaction(name='Local Supermarket', sealed=True)

subd['grc1'] = EntrySubdivision(entry=entry['grc'], transaction=trans['grc'],
                                amount=-3425, description='Meats')

subd['grc2'] = EntrySubdivision(entry=entry['grc'], transaction=trans['grc'],
                                amount=-4260, description='Vegetables')

subd['grc3'] = EntrySubdivision(entry=entry['grc'], transaction=trans['grc'],
                                amount=-2135, description='Grains')

subd['grc4'] = EntrySubdivision(entry=entry['grc'], transaction=trans['grc'],
                                amount=-2225, description='Dairy')

# --------------------

entry['wd1'] = Entry(transactionDate=jan3, postDate=jan3, sealed=True,
                     amount=-6200, account=acct['check'],
                     description='ATM WITHDRAWAL')

entry['wd2'] = Entry(transactionDate=jan3, postDate=jan3, sealed=True,
                     amount=+6000, account=acct['john'],
                     description='ATM WITHDRAWAL')

trans['wd'] = Transaction(name='ATM Withdrawal', sealed=True)

subd['wd1'] = EntrySubdivision(entry=entry['wd1'], transaction=trans['wd'],
                               amount=-6000, description='Withdrawal Amount')

subd['wd2'] = EntrySubdivision(entry=entry['wd1'], transaction=trans['wd'],
                               amount=-200, description='Withdrawal Fee')

subd['wd3'] = EntrySubdivision(entry=entry['wd2'], transaction=trans['wd'],
                               amount=+6000, description='Withdrawal Amount')

# --------------------

entry['gas'] = Entry(transactionDate=jan2, postDate=jan4, sealed=True,
                     amount=-2472, account=acct['creditB'],
                     description='PUMP STATION')

trans['gas'] = Transaction(name='Pump Station', sealed=True)

subd['gas'] = EntrySubdivision(entry=entry['gas'], transaction=trans['gas'],
                               amount=-2472)

# --------------------

entry['rent'] = Entry(transactionDate=jan1, postDate=jan5, sealed=True,
                      amount=-50000, account=acct['check'],
                      description='CHECK #1001')

trans['rent'] = Transaction(name='Rent', sealed=True)

subd['rent'] = EntrySubdivision(entry=entry['rent'], transaction=trans['rent'],
                                amount=-50000)

# --------------------

entry['pmt1'] = Entry(transactionDate=jan5, postDate=jan5, sealed=True,
                      amount=-10000, account=acct['check'],
                      description='CREDIT CARD B ELECTRONIC PAYMENT')

entry['pmt2'] = Entry(transactionDate=jan5, postDate=jan5, sealed=True,
                      amount=+10000, account=acct['check'],
                      description='PAYMENT RECEIVED')

trans['pmt'] = Transaction(name='Credit Card B Payment', sealed=True)

subd['pmt1'] = EntrySubdivision(entry=entry['pmt1'], transaction=trans['pmt'],
                                amount=-10000)

subd['pmt2'] = EntrySubdivision(entry=entry['pmt2'], transaction=trans['pmt'],
                                amount=+10000)

# --------------------

db.session.add_all(entry.values())
db.session.add_all(trans.values())
db.session.add_all(subd.values())

# --------------------------------------------------------------------------------
# Commit the session

db.session.commit()
