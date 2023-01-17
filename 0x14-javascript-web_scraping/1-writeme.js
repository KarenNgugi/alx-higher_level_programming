#!/usr/bin/node

const fs = require('fs');
const file_to_write = process.argv[2];
const text_to_write = process.argv[3];

fs.writeFile(file_to_write, text_to_write, function(err, data) {
  if (err) {
    console.log(err);
  }
});
