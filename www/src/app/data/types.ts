
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

export class Subdivision {
};

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
		this.subdivisions = [];
	}
};

export class UnassignedEntry {
	entry: ExpandedEntry;
	remainingAmount: number;

	constructor(serviceJson) {
		this.entry = new ExpandedEntry(serviceJson.entry);
		this.remainingAmount = serviceJson.remainingAmount;
	}
};

export class Transaction {
	id: number;

	constructor(serviceJson) {
		this.id = serviceJson.id;
	}
};
