import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

export class Subdivision {
};

export class Entry {
	account_id: number;
	amount: number;
	checkNum: number;
	description: string;
	mcc: number;
	memo: string;
	sic: number;
	subdivisions: Subdivision[];
	transactionDate: Date;
	type: string;
	vendorID: string;
};

export class UnassignedEntry {
	entry: Entry;
	remainingAmount: number;
};

@Injectable()
export class TransactionsService {

	constructor(private http: Http) {}

	getUnassignedEntries(): Promise<UnassignedEntry[]> {
		return this.http.get('/api/unassigned-entries')
			.toPromise()
			.then(response => {
				return response.json() as Entry[];
			});
	}
}
