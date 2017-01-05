import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import { UnassignedEntry } from './types';

import 'rxjs/add/operator/toPromise';


@Injectable()
export class TransactionsService {

	constructor(private http: Http) {}

	getUnassignedEntries(): Promise<UnassignedEntry[]> {
		return this.http.get('/api/unassigned-entries')
			.toPromise()
			.then(
				response => response.json().map(
					serviceJson => new UnassignedEntry(serviceJson)
				)
			);
	}
}
