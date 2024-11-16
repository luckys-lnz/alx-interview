#!/usr/bin/node

const request = require("request");

request(
  "https://swapi.dev/api/films/" + process.argv[2],
  function (err, __, body) {
    if (err) throw err;
    const actors = JSON.parse(body).characters;
    exactOrder(actors, 0);
  }
);
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, __, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
