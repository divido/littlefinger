import { Component, OnInit } from '@angular/core';
import { AccountsService } from './data/accounts.service';
import { TransactionsService } from './data/transactions.service';
import { Account, UnassignedEntry } from './data/types';

@Component({
	selector: 'lf-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
	title = 'Littlefinger';

	accounts: Account[];
	unassignedEntries: UnassignedEntry[];
	unassignedMessages: any[] = [];

	constructor(
		private accountsService: AccountsService,
		private transactionsService: TransactionsService) {}

	ngOnInit(): void {
		let entriesPromise: Promise<UnassignedEntry[]> = this.transactionsService.getUnassignedEntries()
			.catch(error => this.unassignedMessages.push({
				severity: 'error',
				summary: 'Could not retrieve unassigned entries',
				detail: error
			})
		);

		let accountsPromise: Promise<Account[]> = this.accountsService.getAccounts()
			.catch(error => this.unassignedMessages.push({
				severity: 'error',
				summary: 'Could not retrieve account information',
				detail: error
			})
		);

		Promise.all<Account[], UnassignedEntry[]>([accountsPromise, entriesPromise]).then(
			results => {
				this.unassignedMessages = [];

				this.accounts = results[0];
				this.unassignedEntries = results[1].sort(
					(a, b) => b.entry.transactionDate.valueOf() - a.entry.transactionDate.valueOf());
			}
		);
	}
}
