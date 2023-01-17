#!/usr/bin/node
var fs = require('fs');
var file = process.argv[2]

fs.readFile(file, 'utf8', function(err, data) {
	if (!err) {
		console.log(data);
	}
	else {
		console.log(err);
	}
});
