import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { TransactionsService } from './data/transactions.service';
import { UnassignedEntryCardComponent } from './unassigned-entry-card/unassigned-entry-card.component';

@NgModule({
	declarations: [
		AppComponent,
		UnassignedEntryCardComponent
	],
	imports: [
		BrowserModule,
		FormsModule,
		HttpModule
	],
	providers: [
		TransactionsService
	],
	bootstrap: [AppComponent]
})
export class AppModule { }
