#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + endpoint;
request(url, function (error, response, body) {
  if (error) {
    console.log('code: ' + response.statusCode);
  } else {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
