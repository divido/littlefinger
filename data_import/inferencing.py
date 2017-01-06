#!/usr/bin/env python3

import logging

from raw import Transaction, EntrySubdivision, Type

# --------------------------------------------------------------------------------

def inferTransactionFromEntry(session, entry):
	"""This method creates a default Transaction and EntrySubdivision for the
	supplied entry, and guesses at a reasonable name and expense category.
	"""

	transaction = Transaction(name=entry.description);
	session.add(transaction);

	unknown = session.query(Type).filter(Type.name == "Unknown").one_or_none();
	if unknown is None:
		unknown = Type(name="Unknown")
		session.add(unknown)

	subdivision = EntrySubdivision(
		entry=entry,
		transaction=transaction,
		type=unknown,
		amount=entry.amount
	);
	session.add(subdivision);
