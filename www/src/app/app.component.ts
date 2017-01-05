import { Component, OnInit } from '@angular/core';
import { TransactionsService, UnassignedEntry } from './data/transactions.service';

@Component({
	selector: 'lf-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
	title = 'Littlefinger';
	unassignedEntries: UnassignedEntry[];

	constructor(private transactionsService: TransactionsService) {}

	ngOnInit(): void {

		this.transactionsService.getUnassignedEntries().then(
			entries => this.unassignedEntries = entries
		).catch(
			error => false
		);
	}
}
