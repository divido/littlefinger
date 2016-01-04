#!/usr/bin/env python3

from eve_sqlalchemy.decorators import registerSchema

from sqlalchemy import func, ForeignKey
from sqlalchemy import Column, String, Integer, DateTime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DOMAIN = {}

# --------------------------------------------------------------------------------

def RegisterTable(tableClass):
    """When creating SQLAlchemy models, they need to be registered with the
    eve_sqlalchemy interface library. Additionally, add the schema to the DOMAIN
    dictionary, which will be used later during construction of the Eve app to
    inform it of which tables to create CRUD interfaces for.
    """

    nm = tableClass.__tablename__
    registerSchema(nm)(tableClass)
    DOMAIN[nm] = tableClass._eve_schema[nm]

# --------------------

def MakeForeignKey(foreignTableClass):
    return Column(Integer, ForeignKey(foreignTableClass.__tablename__ + "._id"))

# --------------------

class TableBase(Base):
    """Define the base functionality for the tables, including the meta-columns
    that are used by Eve, and the value extraction properties.
    """

    __abstract__ = True

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now())
    _etag = Column(String(40))

    @property
    def value(self):
        """This extracts the values of the object into a simple dictionary,
        suitable for passing to jsonify. Values are selected based on the DOMAIN
        schema, established during setup.
        """

        val = {}

        for field in DOMAIN[self.__tablename__]['schema']:
            val[field] = self.__dict__[field]

        return val

    @property
    def expandedValue(self):
        """This is a hook to allow tables to inject additional entries beyond
        those provided in the schema. This is intended to be used for composed
        objects, so that the expanded value dictionary also contains all the
        expanded values of contained objects, recursively.
        """

        return self.value
