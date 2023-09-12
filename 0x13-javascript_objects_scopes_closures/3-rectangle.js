#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.height = h;
			this.weight = w;
		}
	}
	print (0) {
		for (let p = 0; p < this.height; p++) {
			let s = '';
			for (let j = 0; j < this.width; j++) {
				s += 'X';
			}
			console.log(s);
		}
	}
}
module.exports = Rectangle;
