#!/usr/bin/env python3

from sqlalchemy import Column, String, Text

from .table_base import TableBase, RegisterTable

# --------------------------------------------------------------------------------

class Type(TableBase):
    """A Type is used to categorize expenses. Types can be any short string, and
    subtypes are created by using a dot to separate (such as
    "Health.Vitamins"). Each EntrySubdivision should contain exactly one Type to
    categorize that part of the Entry.
    """

    _singular = 'type'
    _plural = 'types'
    __tablename__ = _plural

    name = Column(String(64))
    description = Column(Text)

RegisterTable(Type)
