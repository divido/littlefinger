
import { Component, Input, OnInit } from '@angular/core';

import { Account, UnassignedEntry } from '../data/types';

@Component({
	selector: 'lf-unassigned-entry-card',
	templateUrl: './unassigned-entry-card.component.html',
	styleUrls: ['./unassigned-entry-card.component.scss']
})
export class UnassignedEntryCardComponent implements OnInit {
	@Input()
	unassigned: UnassignedEntry;

	@Input()
	accounts: Account[];

	accountName: string;

	constructor() {}

	ngOnInit() {
		this.accounts.forEach(account => {
			if (account.id === this.unassigned.entry.account_id) {
				this.accountName = account.name;
			}
		});
	}
}
