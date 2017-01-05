
export class Subdivision {
};

export class Entry {
	account_id: number;
	amount: number;
	checkNum: number;
	description: string;
	mcc: number;
	memo: string;
	sic: number;
	transactionDate: Date;
	type: string;
	vendorID: string;

	constructor(serviceJson) {
		this.account_id = serviceJson.account_id;
		this.amount = serviceJson.amount;
		this.checkNum = serviceJson.checkNum;
		this.description = serviceJson.description;
		this.mcc = serviceJson.mcc;
		this.memo = serviceJson.memo;
		this.sic = serviceJson.sic;
		this.transactionDate = new Date(serviceJson.transactionDate);
		this.type = serviceJson.type;
		this.vendorID = serviceJson.vendorID;
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
