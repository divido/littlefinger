import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import { Type } from './types';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class TypesService {
	cache: Promise<Type[]>;

	constructor(private http: Http) {}

	getTypes(): Promise<Type[]> {
		if (! this.cache) {
			this.cache = this.http.get('/api/types')
				.toPromise()
				.then(response => response.json().map(
					serviceJson => new Type(serviceJson)));
		}

		return this.cache;
	}
}
