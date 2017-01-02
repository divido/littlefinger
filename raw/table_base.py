#!/usr/bin/env python3

from eve_sqlalchemy.decorators import registerSchema

from sqlalchemy import func, ForeignKey
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

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

def MakeParentChild(parentClass, childClass):
	"""Establishes a parent-child relationship between the two table classes
	listed. The child will add a database column, named based on the parent's
	singular form (such as 'account_id'), as well as a relationship back
	reference for programmatic access ('account', in this case). The parent gets
	a plural form relationship (e.g., 'entries'). Additionally, this sets some
	class variables to automatically expand the children when printing in
	expanded form. See expandedValue (in TableBase), below.
	"""

	setattr(childClass, parentClass._singular + '_id',
			Column(Integer, ForeignKey(parentClass.__tablename__ + '._id')))

	setattr(parentClass, childClass._plural,
			relationship(childClass, backref=parentClass._singular, lazy='dynamic'))

	if not hasattr(parentClass, '_expandedFields'):
		parentClass._expandedFields = []

	parentClass._expandedFields.append(childClass._plural)

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
			val[field] = getattr(self, field)

		return val

	@property
	def expandedValue(self):
		"""This injects additional items into the dictionary, based on the
		relationships established from MakeParentChild. If the special
		_expandedFields attribute is found on the class-level, it is used to
		figure out the children and recursively expand their content.
		"""

		val = self.value

		if hasattr(self.__class__, '_expandedFields'):
			for field in self.__class__._expandedFields:
				val[field] = [item.expandedValue for item in getattr(self, field).all()]

		return val
