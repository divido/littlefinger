import { Component, OnInit } from '@angular/core';
import { AccountsService } from './data/accounts.service';
import { TransactionsService } from './data/transactions.service';
import { Account, ExpandedTransaction } from './data/types';

@Component({
	selector: 'lf-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
	title = 'Littlefinger';

	unapproved: ExpandedTransaction[];
	unapprovedMessages: any[] = [];

	constructor(
		private accountsService: AccountsService,
		private transactionsService: TransactionsService) {}

	ngOnInit(): void {
		this.accountsService.getAccounts()
			.catch(error => this.unapprovedMessages.push({
				severity: 'error',
				summary: 'Could not retrieve account information',
				detail: error
			})
		);

		this.transactionsService.getUnapprovedTransactions()
			.then(results => this.unapproved = results)
			.catch(error => this.unapprovedMessages.push({
				severity: 'error',
				summary: 'Could not retrieve unapproved transactions',
				detail: error
			})
		);
	}
}
