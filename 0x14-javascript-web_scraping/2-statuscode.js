#!/usr/bin/node

const request = require('request');
const site = process.argv[2];

request(site, function(err, data) {
	if (!err) {
		console.log('code:', data.statusCode);
	}
	else {
		console.log(err);
	}
});
