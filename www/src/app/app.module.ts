import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { MessagesModule } from 'primeng/primeng';

import { AccountsService } from './data/accounts.service';
import { TransactionsService } from './data/transactions.service';

import { AppComponent } from './app.component';
import { UnassignedEntryCardComponent } from './unassigned-entry-card/unassigned-entry-card.component';

@NgModule({
	declarations: [
		AppComponent,
		UnassignedEntryCardComponent
	],
	imports: [
		BrowserModule,
		FormsModule,
		HttpModule,
		MessagesModule
	],
	providers: [
		AccountsService,
		TransactionsService
	],
	bootstrap: [AppComponent]
})
export class AppModule { }
