#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, Boolean, DateTime

from .table_base import TableBase, RegisterTable, MakeParentChild
from .accounts import Account

# --------------------------------------------------------------------------------

class Transaction(TableBase):
    _singular = 'transaction'
    _plural = 'transactions'
    __tablename__ = _plural

    name = Column(String(256))
    description = Column(String(256))
    sealed = Column(Boolean)

RegisterTable(Transaction)

# --------------------

class Entry(TableBase):
    _singular = 'entry'
    _plural = 'entries'
    __tablename__ = _plural

    transactionDate = Column(DateTime)
    postDate = Column(DateTime)
    description = Column(String(256))
    amount = Column(Integer)
    sealed = Column(Boolean)

MakeParentChild(Account, Entry)
RegisterTable(Entry)

# --------------------

class EntrySubdivision(TableBase):
    _singular = 'subdivision'
    _plural = 'subdivisions'
    __tablename__ = _plural

    description = Column(String(256))
    amount = Column(Integer)

MakeParentChild(Entry, EntrySubdivision)
MakeParentChild(Transaction, EntrySubdivision)
RegisterTable(EntrySubdivision)
