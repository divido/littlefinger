#!/usr/bin/env python3

from sqlalchemy import Column, String

from .table_base import TableBase, RegisterTable

# --------------------------------------------------------------------------------

class User(TableBase):
    _singular = 'user'
    _plural = 'users'
    __tablename__ = _plural

    username = Column(String(80))
    display = Column(String(80))

RegisterTable(User)
