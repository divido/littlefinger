import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import { ExpandedTransaction } from './types';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class TransactionsService {
	cache: Promise<ExpandedTransaction[]>;

	constructor(private http: Http) {}

	getUnapprovedTransactions(): Promise<ExpandedTransaction[]> {
		if (! this.cache) {
			this.cache = this.http.get('/api/transactions/unapproved')
				.toPromise()
				.then(response => response.json().map(
					serviceJson => new ExpandedTransaction(serviceJson)));
		}

		return this.cache;
	}
}
