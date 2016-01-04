#!/usr/bin/env python3

from sqlalchemy import Column, String

from .table_base import TableBase, RegisterTable

# --------------------------------------------------------------------------------

class User(TableBase):
    __tablename__ = 'user'

    username = Column(String(80))
    display = Column(String(80))

RegisterTable(User)
