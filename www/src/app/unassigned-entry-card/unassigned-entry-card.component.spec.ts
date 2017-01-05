/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { UnassignedEntryCardComponent } from './unassigned-entry-card.component';

describe('UnassignedEntryCardComponent', () => {
	let component: UnassignedEntryCardComponent;
	let fixture: ComponentFixture<UnassignedEntryCardComponent>;

	beforeEach(async(() => {
		TestBed.configureTestingModule({
			declarations: [ UnassignedEntryCardComponent ]
		})
			.compileComponents();
	}));

	beforeEach(() => {
		fixture = TestBed.createComponent(UnassignedEntryCardComponent);
		component = fixture.componentInstance;
		fixture.detectChanges();
	});

	it('should create', () => {
		expect(component).toBeTruthy();
	});
});
