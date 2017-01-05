import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import { Account } from './types';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class AccountsService {

	constructor(private http: Http) {}

	getAccounts(): Promise<Account[]> {
		return this.http.get('/api/accounts')
			.toPromise()
			.then(
				response => response.json().map(
					serviceJson => new Account(serviceJson)
				)
			);
	}
}
