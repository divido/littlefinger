import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { ButtonModule } from 'primeng/primeng';
import { EditorModule } from 'primeng/primeng';
import { InplaceModule } from 'primeng/primeng';
import { InputTextModule } from 'primeng/primeng';
import { MessagesModule } from 'primeng/primeng';
import { SharedModule } from 'primeng/primeng';

import { AccountsService } from './data/accounts.service';
import { EntriesService } from './data/entries.service';
import { TransactionsService } from './data/transactions.service';
import { TypesService } from './data/types.service';

import { AppComponent } from './app.component';
import { TransactionCardComponent } from './transaction-card/transaction-card.component';

@NgModule({
	declarations: [
		AppComponent,
		TransactionCardComponent
	],
	imports: [
		BrowserModule,
		FormsModule,
		HttpModule,
		ButtonModule,
		EditorModule,
		InplaceModule,
		InputTextModule,
		MessagesModule,
		SharedModule
	],
	providers: [
		AccountsService,
		EntriesService,
		TransactionsService,
		TypesService
	],
	bootstrap: [AppComponent]
})
export class AppModule { }
