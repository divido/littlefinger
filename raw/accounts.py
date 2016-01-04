#!/usr/bin/env python3

from sqlalchemy import Column, String, Enum

from .table_base import TableBase, RegisterTable

# --------------------------------------------------------------------------------

class Account(TableBase):
    __tablename__ = 'account'

    name = Column(String(80))
    kind = Column(Enum(
        'checking',
        'savings',
        'cash',
        'credit',
        'friendly'
    ))

    @property
    def expandedValue(self):
        val = self.value
        val['entries'] = [item.expandedValue for item in self.entries.all()]
        return val

RegisterTable(Account)
