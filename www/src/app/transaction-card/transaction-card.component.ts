import { Component, Input, OnInit } from '@angular/core';

import { AppComponent } from '../app.component';
import { Account, AccountMap } from '../data/types';
import { Entry, EntryMap } from '../data/types';
import { ExpandedTransaction } from '../data/types';
import { Subdivision } from '../data/types';
import { Type, TypeMap } from '../data/types';

import { AccountsService } from '../data/accounts.service';
import { EntriesService } from '../data/entries.service';
import { TransactionsService } from '../data/transactions.service';
import { TypesService } from '../data/types.service';

import { buildMap } from '../data/map-builder';

// --------------------------------------------------------------------------------

interface SubdivisionGroup {
	entry: Entry;
	account: Account;
	subdivisions: [{
		type: Type,
		data: Subdivision
	}];
};

// ----------------------------------------

@Component({
	selector: 'lf-transaction-card',
	templateUrl: './transaction-card.component.html',
	styleUrls: ['./transaction-card.component.scss']
})
export class TransactionCardComponent implements OnInit {
	@Input()
	transaction: ExpandedTransaction;

	// ----------------------------------------

	dates: Date[] = [];
	subdivisionGroups: SubdivisionGroup[] = [];
	totalAmount: number;
	approve: boolean = false;

	// ----------------------------------------

	constructor(
		private accountsService: AccountsService,
		private entriesService: EntriesService,
		private typesService: TypesService) {}

	ngOnInit(): void {
		this.totalAmount = this.transaction.subdivisions.reduce(
			(accumulated, subdivision) => accumulated + subdivision.amount, 0);

		let accounts: AccountMap;
		let entries: EntryMap;
		let types: TypeMap;

		let accountsPromise = this.accountsService.getAccounts().then(
			accountsArray => accounts = buildMap(accountsArray));

		let entriesPromise = this.entriesService.getEntries().then(
			entriesArray => entries = buildMap(entriesArray));

		let typesPromise = this.typesService.getTypes().then(
			typesArray => types = buildMap(typesArray));

		// --------------------

		entriesPromise.then(() => this.extractDates(entries));

		Promise.all([accountsPromise, entriesPromise, typesPromise]).then(
			() => this.extractSubdivisionData(entries, accounts, types));
	}

	extractDates(entries: EntryMap) {
		// Grab all dates, sans time information
		let entryDates = this.transaction.subdivisions.map(subdivision => {
			let date = entries[subdivision.entry_id].transactionDate;
			return new Date(date.getFullYear(), date.getMonth(), date.getDate());
		}).sort((a, b) => b.valueOf() - a.valueOf());

		// This approximates a unique function for sorted data
		this.dates = [];
		let len = 0;

		entryDates.forEach(date => {
			if (len === 0 || this.dates[len - 1] !== date) {
				this.dates.push(date);
				len++;
			}
		});
	}

	extractSubdivisionData(entries: EntryMap, accounts: AccountMap, types: TypeMap) {
		this.transaction.subdivisions.forEach(subdivision => {
			let associatedGroup = null;

			this.subdivisionGroups.forEach(group => {
				if (group.entry.id === subdivision.entry_id) {
					associatedGroup = group;
				}
			});

			if (associatedGroup === null) {
				associatedGroup = {
					entry: entries[subdivision.entry_id],
					account: accounts[entries[subdivision.entry_id].account_id],
					subdivisions: []
				};

				this.subdivisionGroups.push(associatedGroup);
			}

			associatedGroup.subdivisions.push({
				type: types[subdivision.type_id],
				data: subdivision
			});
		});
	}
}
