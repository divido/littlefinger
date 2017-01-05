
import { Component, Input, OnInit } from '@angular/core';

import { UnassignedEntry } from '../data/types';

@Component({
	selector: 'lf-unassigned-entry-card',
	templateUrl: './unassigned-entry-card.component.html',
	styleUrls: ['./unassigned-entry-card.component.scss']
})
export class UnassignedEntryCardComponent implements OnInit {
	@Input()
	entry: UnassignedEntry;

	constructor() {}

	ngOnInit() {
	}
}
