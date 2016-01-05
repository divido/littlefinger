#!/usr/bin/env python3

from sqlalchemy import Column, Text, Enum

from .table_base import TableBase, RegisterTable, MakeParentChild
from .server_info import User
from .transactions import Transaction

# --------------------------------------------------------------------------------

class Comment(TableBase):
    """This represents a single Comment in a stream of commentary on a given
    Transaction. Comments with null values for users represent changes made
    automatically by the system. Users can thereafter make further
    modifications, add textual commentary, express approval of the pending
    transaction, or revoke such approval.

    The approvals are used to transition a transaction from the pending status
    to a sealed status. When all users have expressed approval more recently
    than any modification, the transaction automatically transitions into a
    sealed state.

    It can be reopened again with another modification, which then requires all
    users to re-approve the modification to regain sealed status. The API must
    maintain consistency between the commentary and the sealed flag on the
    Transaction.
    """

    _singular = 'comment'
    _plural = 'comments'
    __tablename__ = _plural

    comments = Column(Text)
    kind = Column(Enum(
        'text',
        'modification',
        'approval',
        'disapproval'
    ))

MakeParentChild(User, Comment)
MakeParentChild(Transaction, Comment)

RegisterTable(Comment)
