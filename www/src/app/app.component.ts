import { Component, OnInit } from '@angular/core';
import { TransactionsService } from './transactions.service';

@Component({
	selector: 'littlefinger-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {
	title = 'Littlefinger works!';
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
