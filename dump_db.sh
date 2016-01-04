#!/bin/bash

sqlite3.exe -batch data.sqlite <<EOF
.mode column
.header on
.null (null)

.system echo '~~~~ Users ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 8 8
select _id, username, display from users;

.system echo
.system echo '~~~~ Accounts ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 16 8
select _id, name, kind from accounts;

.system echo
.system echo '~~~~ Transactions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 20 20 6
select _id, name, description, sealed from transactions;

.system echo
.system echo '~~~~ Entries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 10 10 20 -6 6 8
select _id, transactionDate as tranDate, postDate, description, amount, sealed, account_id as acct_id from entries;

.system echo
.system echo '~~~~ Subdivisions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
.width 4 20 -6 8 8
select _id, description, amount, entry_id, transaction_id as tran_id from subdivisions;

EOF
