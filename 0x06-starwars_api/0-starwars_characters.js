#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];
async function starwarsCharacters (filmId) {
  try {
    const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    const filmResponse = await request(endpoint);
    const film = JSON.parse(filmResponse.body);
    const characters = film.characters;
    const results = [];
    const characterRequests = characters.map(async (urlCharacter, i) => {
      try {
        const characterResponse = await request(urlCharacter);
        const character = JSON.parse(characterResponse.body);
        results[i] = character.name;
      } catch (characterError) {
        console.error(`Error fetching character: ${urlCharacter}`, characterError.message);
      }
    });
    await Promise.all(characterRequests);
    results.map(name => console.log(name));
  } catch (filmError) {
    console.error(`Error fetching film details: ${filmId}`, filmError.message);
  }
}
starwarsCharacters(filmID);
