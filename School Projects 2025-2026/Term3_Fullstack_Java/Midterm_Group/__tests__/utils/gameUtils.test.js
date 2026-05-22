const {
  getGamesByGenre,
  getTopRatedGames,
  getGameDetailsById,
  selectRandomGameId,
  getHiddenGems,
} = require("../../utils/gameUtils");
const { Genres } = require("../../utils/data");

describe("Game Utility Functions", () => {
  describe("getGamesByGenre", () => {
    test("Should grab first game in list with given genre", () => {
      const result = getGamesByGenre(Genres.ADVENTURE);
      expect(result[0]).toEqual({
        id: 0,
        title: "The Legend of Zelda: Breath of the Wild",
        description: "An open-world action-adventure game set in Hyrule.",
        developer: "Nintendo",
        releaseYear: 2017,
        genre: "Adventure",
        averageRating: 9.8,
        numberOfReviews: 12000,
        released: true,
        image: "/images/gameImages/LOZBreathOfTheWild.jpg",
      });
    });
  });

  describe("getTopRatedGames", () => {
    test("Should grab games with highest ratings with 5000 reviews or more", () => {
      const result = getTopRatedGames();
      expect(result[0]).toEqual({
        id: 0,
        title: "The Legend of Zelda: Breath of the Wild",
        description: "An open-world action-adventure game set in Hyrule.",
        developer: "Nintendo",
        releaseYear: 2017,
        genre: "Adventure",
        averageRating: 9.8,
        numberOfReviews: 12000,
        released: true,
        image: "/images/gameImages/LOZBreathOfTheWild.jpg",
      });
    });
  });

  describe("getGameDetailsById", () => {
    test("Should grab the game with correct ID", () => {
      const result = getGameDetailsById(1);
      expect(result).toEqual({
        id: 1,
        title: "The Witcher 3: Wild Hunt",
        description:
          "A sprawling RPG filled with monsters, magic, and rich storytelling.",
        developer: "CD Projekt Red",
        releaseYear: 2015,
        genre: "Role-Play",
        averageRating: 9.7,
        numberOfReviews: 15000,
        released: true,
        image: "/images/gameImages/TheWitcher3WildHunt.jpg",
      });
    });
  });

  describe("selectRandomGameId", () => {
  test("Should return a random game object", () => {
    const result = selectRandomGameId();

    expect(result).toBeTruthy();
    expect(typeof result).toBe("object");

    expect(result).toEqual(
      expect.objectContaining({
        id: expect.any(Number),
        title: expect.any(String),
        description: expect.any(String),
        developer: expect.any(String),
        releaseYear: expect.any(Number),
        genre: expect.any(String),
        averageRating: expect.any(Number),
        numberOfReviews: expect.any(Number),
        released: expect.any(Boolean),
        image: expect.any(String),
      })
    );
  });
});

  describe("getHiddenGems", () => {
    test("Grab first item in list that fits hidden gem criteria", () => {
      const result = getHiddenGems();
      expect(result[0]).toEqual({
        id: 9,
        title: "Disco Elysium",
        description:
          "A narrative-driven RPG where you play as a detective with unique skill-based dialogue.",
        developer: "ZA/UM",
        releaseYear: 2019,
        genre: "Role-Play",
        averageRating: 9.6,
        numberOfReviews: 950,
        released: true,
        image: "/images/gameImages/DiscoElysium.jpg",
      });
    });
  });
});
