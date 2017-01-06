interface HasID {
	id: number;
};

export function buildMap<DataType extends HasID>(array: DataType[]): {[id: number]: DataType} {
	let map: {[id: number]: DataType} = {};
	array.forEach(elem => map[elem.id] = elem);
	return map;
};
