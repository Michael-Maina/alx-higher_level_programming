#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const fs = require('fs');
      const fileName = process.argv[3];
      fs.writeFile(fileName, body, 'utf-8', function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  }
});
