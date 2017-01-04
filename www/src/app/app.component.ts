import { Component, OnInit } from '@angular/core';
import { TransactionsService } from './data/transactions.service';

@Component({
	selector: 'littlefinger-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
	title = 'Littlefinger';
	unassignedEntries: string;

	constructor(private transactionsService: TransactionsService) {}

	ngOnInit(): void {
		this.transactionsService.getUnassignedEntries().then(
			entries => this.unassignedEntries = JSON.stringify(entries, null, 2)
		).catch(
			error => this.unassignedEntries = error
		);
	}
}
