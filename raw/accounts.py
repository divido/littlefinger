#!/usr/bin/env python3

from sqlalchemy import Column, String, Enum

from .table_base import TableBase, RegisterTable

# --------------------------------------------------------------------------------

class Account(TableBase):
    _singular = 'account'
    _plural = 'accounts'
    __tablename__ = _plural

    name = Column(String(80))
    kind = Column(Enum(
        'checking',
        'savings',
        'cash',
        'credit',
        'friendly'
    ))

RegisterTable(Account)