#!/usr/bin/env python3

from . import db

# --------------------------------------------------------------------------------

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
			db.Column(db.Integer, db.ForeignKey(parentClass.__tablename__ + '.id')))

	setattr(parentClass, childClass._plural,
			db.relationship(childClass, backref=parentClass._singular, lazy='dynamic'))

	if not hasattr(parentClass, '_expandedFields'):
		parentClass._expandedFields = []

	parentClass._expandedFields.append(childClass._plural)

# --------------------

class TableBase(db.Model):
	"""Define the base functionality for the tables, including a simple primary
	key and method to convert into a simple (or extended) dictionary class,
	suitalble for JSON conversion.
	"""

	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)

	@property
	def value(self):
		"""This extracts the values of the object into a simple dictionary,
		suitable for passing to jsonify. Values are selected based on __table__
		object, which is created & managed by SQLAlchemy
		"""

		val = {}

		for column in self.__table__.columns:
			val[column.key] = getattr(self, column.key)

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
