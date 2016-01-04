#!/bin/bash

sqlite3.exe -batch data.sqlite <<EOF
.mode column
.header on
.null (null)

.system echo '~~~~ User ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 8 8
select _id, username, display from user;

.system echo
.system echo '~~~~ Account ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 16 8
select _id, name, kind from account;

.system echo
.system echo '~~~~ Transaction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 20 20 6
select _id, name, description, sealed from _transaction;

.system echo
.system echo '~~~~ Entry ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 10 10 20 -6 6 8
select _id, transactionDate as tranDate, postDate, description, amount, sealed, account_id as acct_id from entry;

.system echo
.system echo '~~~~ Subdivision ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 20 -6 8 8
select _id, description, amount, entry_id, transaction_id as tran_id from entry_subdivision;

EOF
