const { VideoGames, Genres } = require("./data");

/**
 * Get `x` games by genre
 * @param {string} genre - The genre of the games
 * @param {number} x - The number of games to retrieve
 * @returns {*} - An array of games matching the genre
 */
function getGamesByGenre(genre, x) {
  const genreGames = VideoGames.filter((game) => game.genre === genre);
  return genreGames.slice(0, x);
}

/**
 * Get the `x` top-rated games, ordered by rating
 * @param {number} x - The number of top-rated games to retrieve
 * @returns {*} - An array of top-rated games
 */
function getTopRatedGames(x) {
  const topRated = VideoGames.filter(
    (game) => game.averageRating > 8.5 && game.numberOfReviews > 4999
  );
  const topRatedSort = topRated.sort(
    (a, b) => b.averageRating - a.averageRating
  );
  return topRatedSort.slice(0, x);
}

/**
 * Get the details of a game by its ID
 * @param {number} id - The ID of the game
 * @returns {*} - The game object
 */
function getGameDetailsById(id) {
  const gameID = VideoGames[id];
  return gameID;
}

/**
 * Select a random game ID
 * @returns {*} - A random game ID
 */
function selectRandomGameId() {
  const randID = Math.floor(Math.random() * VideoGames.length);
  const randGame = VideoGames[randID];
  return randGame;
}

/**
 * Get "Hidden Gems" - games that are highly rated but not widely reviewed
 * @returns {*} - An array of hidden gem games
 */
function getHiddenGems(x) {
  const topRated = VideoGames.filter(
    (game) => game.averageRating > 9.5 && game.numberOfReviews < 5000
  );
  return topRated.slice(0, x);
}

function getUnreleased() {
  const unreleased = VideoGames.filter((game) => game.released === false);
  return unreleased;
}

function homeRandom(x) {
  const homeGames = [...VideoGames].sort(() => 0.5 - Math.random());
  return homeGames.slice(0, x);
}

// Export the functions to be used in other modules
module.exports = {
  getGamesByGenre,
  getTopRatedGames,
  getGameDetailsById,
  selectRandomGameId,
  getHiddenGems,
  getUnreleased,
  homeRandom,
};