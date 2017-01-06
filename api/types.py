#!/usr/bin/env python3

import logging

from raw import db, Type

# --------------------------------------------------------------------------------

def types():
	"""Retrieves all type information from the database and returns them
	"""
	return [item.value for item in db.session.query(Type).all()]
