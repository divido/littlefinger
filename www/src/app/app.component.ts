import { Component, OnInit } from '@angular/core';
import { TransactionsService } from './data/transactions.service';
import { UnassignedEntry } from './data/types';

@Component({
	selector: 'lf-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
	title = 'Littlefinger';

	unassignedEntries: UnassignedEntry[];
	unassignedMessages: any[] = [];

	constructor(private transactionsService: TransactionsService) {}

	ngOnInit(): void {

		this.transactionsService.getUnassignedEntries().then(
			entries => {
				this.unassignedMessages = [];
				this.unassignedEntries = entries.sort(
					(a, b) => b.entry.transactionDate.valueOf() - a.entry.transactionDate.valueOf());
			}
		).catch(
			error => this.unassignedMessages.push({
				severity: 'error',
				summary: 'Could not retrieve unassigned entries',
				detail: error
			})
		);
	}
}
