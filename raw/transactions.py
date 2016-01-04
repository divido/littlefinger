#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship

from .table_base import TableBase, RegisterTable, MakeForeignKey
from .accounts import Account

# --------------------------------------------------------------------------------

class Transaction(TableBase):
    __tablename__ = '_transaction'

    name = Column(String(256))
    description = Column(String(256))
    sealed = Column(Boolean)

    @property
    def expandedValue(self):
        val = self.value
        val['subdivisions'] = [item.expandedValue for item in self.subdivisions.all()]
        return val

RegisterTable(Transaction)

# --------------------

class Entry(TableBase):
    __tablename__ = 'entry'

    transactionDate = Column(DateTime)
    postDate = Column(DateTime)
    description = Column(String(256))
    amount = Column(Integer)
    sealed = Column(Boolean)

    account_id = MakeForeignKey(Account)

    @property
    def expandedValue(self):
        val = self.value
        val['subdivisions'] = [item.expandedValue for item in self.subdivisions.all()]
        return val

RegisterTable(Entry)
Account.entries = relationship(Entry, backref='account', lazy='dynamic')

# --------------------

class EntrySubdivision(TableBase):
    __tablename__ = 'entry_subdivision'

    description = Column(String(256))
    amount = Column(Integer)

    entry_id = MakeForeignKey(Entry)
    transaction_id = MakeForeignKey(Transaction)

RegisterTable(EntrySubdivision)
Entry.subdivisions = relationship(EntrySubdivision, backref='entry', lazy='dynamic')
Transaction.subdivisions = relationship(EntrySubdivision, backref='transaction', lazy='dynamic')
