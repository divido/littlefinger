import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import { Entry } from './types';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class EntriesService {
	cache: Promise<Entry[]>;

	constructor(private http: Http) {}

	getEntries(): Promise<Entry[]> {
		if (! this.cache) {
			this.cache = this.http.get('/api/entries')
				.toPromise()
				.then(response => response.json().map(
					serviceJson => new Entry(serviceJson)));
		}

		return this.cache;
	}
}
