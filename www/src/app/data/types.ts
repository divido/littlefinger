
export class Account {
	id: number;
	name: string;
	kind: string;
	accountNumber: number;

	lastImport: Date;
	ofxID: string;

	constructor(serviceJson) {
		this.id = serviceJson.id;
		this.name = serviceJson.name;
		this.kind = serviceJson.kind;
		this.accountNumber = serviceJson.number;
		this.lastImport = new Date(serviceJson.lastImport);
		this.ofxID = serviceJson.ofxID;
	}
};

export interface AccountMap {
	[id: number]: Account;
};

// --------------------------------------------------------------------------------

export class Type {
	id: number;
	name: string;
	description: string;

	constructor(serviceJson) {
		this.id = serviceJson.id;
		this.name = serviceJson.name;
		this.description = serviceJson.description;
	}
};

export interface TypeMap {
	[id: number]: Type;
};

// --------------------------------------------------------------------------------

export class Subdivision {
	id: number;
	description: string;
	amount: number;

	entry_id: number;
	transaction_id: number;
	type_id: number;

	constructor(serviceJson) {
		this.id = serviceJson.id;
		this.description = serviceJson.description;
		this.amount = serviceJson.amount;

		this.entry_id = serviceJson.entry_id;
		this.transaction_id = serviceJson.transaction_id;
		this.type_id = serviceJson.type_id;
	}
};

// --------------------------------------------------------------------------------

export class Entry {
	id: number;
	account_id: number;
	vendorID: string;

	amount: number;
	transactionDate: Date;

	checkNum: number;
	description: string;
	memo: string;

	type: string;
	mcc: number;
	sic: number;

	constructor(serviceJson) {
		this.id = serviceJson.id;
		this.account_id = serviceJson.account_id;
		this.vendorID = serviceJson.vendorID;

		this.amount = serviceJson.amount;
		this.transactionDate = new Date(serviceJson.transactionDate);

		this.checkNum = serviceJson.checkNum;
		this.description = serviceJson.description;
		this.memo = serviceJson.memo;

		this.type = serviceJson.type;
		this.mcc = serviceJson.mcc;
		this.sic = serviceJson.sic;
	}
};

export class ExpandedEntry extends Entry {
	subdivisions: Subdivision[];

	constructor(serviceJson) {
		super(serviceJson);
		this.subdivisions = serviceJson.subdivisions.map(subdiv => new Subdivision(subdiv));
	}
};

export interface EntryMap {
	[id: number]: Entry;
};

// --------------------------------------------------------------------------------

export class Transaction {
	id: number;
	name: string;
	description: string;

	constructor(serviceJson) {
		this.id = serviceJson.id;
		this.name = serviceJson.name;
		this.description = serviceJson.description;
	}
};

export class ExpandedTransaction extends Transaction {
	subdivisions: Subdivision[];

	constructor(serviceJson) {
		super(serviceJson);
		this.subdivisions = serviceJson.subdivisions.map(subdiv => new Subdivision(subdiv));
	}
};

export interface ExpandedTransactionMap {
	[id: number]: ExpandedTransaction;
};
