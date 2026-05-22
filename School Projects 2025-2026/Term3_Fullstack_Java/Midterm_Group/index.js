const express = require("express");
const path = require("path");
const { VideoGames, Genres } = require("./utils/data");
const {
  getGameDetailsById,
  getGamesByGenre,
  getTopRatedGames,
  selectRandomGameId,
  getHiddenGems,
  getUnreleased,
  homeRandom,
} = require("./utils/gameUtils");

const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static("public"));

// routes

// home page
app.get("/", (request, response) => {
  const homePageGames = homeRandom(9);
  response.render("index", {
    VideoGames: homePageGames,
    showDescription: false,
  });
});

// games library and filtering
app.get("/games", (request, response) => {
  const genre = request.query.genre;

  if (genre === undefined) {
    response.render("gameLibrary", {
      VideoGames,
      Genres,
      Genre: null,
      showDescription: true,
    });
  } else {
    const games = getGamesByGenre(genre, 100);
    response.render("gameLibrary", {
      VideoGames: games,
      Genres,
      Genre: genre,
      showDescription: true,
    });
  }
});

// game details route
app.get("/game/:id", (request, response) => {
  const id = parseInt(request.params.id);
  const game = getGameDetailsById(id);

  if (!game) {
    return response.status(404).send("Game not found");
  }

  const sameGenreGames = VideoGames.filter(
    (g) => g.genre === game.genre && g.id !== game.id
  );

  const shuffled = sameGenreGames.sort(() => 0.5 - Math.random());
  const recommendedGames = shuffled.slice(0, 3);
  response.render("gameDetails", {
    game,
    recommendedGames,
    showDescription: false,
  });
});

// hidden gems
app.get("/hiddenGems", (request, response) => {
  const hiddenGemGames = getHiddenGems(VideoGames.length);
  response.render("hiddenGems", {
    VideoGames: hiddenGemGames,
    showDescription: true,
  });
});

// top rated
app.get("/topRated", (request, response) => {
  const topRatedGames = getTopRatedGames(15);
  response.render("topRated", {
    VideoGames: topRatedGames,
    showDescription: true,
  });
});

// upcoming
app.get("/upcoming", (request, response) => {
  const upcomingGames = getUnreleased();
  response.render("upcoming", {
    VideoGames: upcomingGames,
    showDescription: true,
  });
});

// random game route
app.get("/random", (request, response) => {
  const randGame = selectRandomGameId();
  const gameIndex = VideoGames.indexOf(randGame);

  if (gameIndex === -1) {
    return response.status(404).send("Game not found");
  }

  response.redirect(`/game/${gameIndex}`);
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
