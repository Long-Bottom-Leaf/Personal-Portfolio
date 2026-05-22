// ============================
//  Express + Mongoose CD API
// ============================

const express = require('express');
const mongoose = require('mongoose');
const app = express();
const PORT = 3000;

app.use(express.json());

// ============================
//  CD Model
// ============================

const cdSchema = new mongoose.Schema({
  title: { type: String, required: true },
  artist: { type: String, required: true },
  genre: { type: String, required: true },
  year: { type: Number, required: true },
});

const CD = mongoose.model("CD", cdSchema);

// ============================
//  Routes
// ============================

// GET /cds - Return all CDs
app.get('/cds', async (request, response) => {
  try {
    let query = {};
    
    // Filtering by artist
    if (request.query.artist) {
      query.artist = request.query.artist;
    }

    // Filtering by genre
    if (request.query.genre) {
      query.genre = request.query.genre;
    }

    // Filtering by year (specific year and before year)
    if (request.query.year) {
      query.year = parseInt(request.query.year);
    }

    if (request.query.before) {
      query.year = { $lte: parseInt(request.query.before) };
    }

    // Field selection
    let fields = null;
    if (request.query.fields) {
      fields = request.query.fields.split(',').join(' ');
    }

    const cds = await CD.find(query).select(fields);
    response.json(cds);

  } catch (error) {
    response.status(500).json({ error: "Error fetching CDs" });
  }
});

// POST /cds - Add a new CD
app.post('/cds', async (request, response) => {
  try {
    const { title, artist, genre, year } = request.body;

    if (!title || !artist || !genre || !year) {
      return response.status(400).json({ error: "All fields are required" });
    }

    const newCd = new CD({ title, artist, genre, year });

    // save cd to database
    await newCd.save();
    response.status(201).json(newCd);

  } catch (error) {
    response.status(500).json({ error: "Error adding CD" });
  }
});

// PUT /cds/:id - Update an existing CD
app.put('/cds/:id', async (request, response) => {
  try {
    const updatedCd = await CD.findByIdAndUpdate(
      request.params.id,
      request.body,
      { new: true, runValidators: true }
    );

    if (!updatedCd) {
      return response.status(404).json({ error: "CD not found" });
    }

    response.json(updatedCd);

  } catch (error) {
    response.status(500).json({ error: "Error updating CD" });
  }
});

// DELETE /cds/:id - Delete a CD
app.delete('/cds/:id', async (request, response) => {
  try {
    const deletedCd = await CD.findByIdAndDelete(request.params.id);

    if (!deletedCd) {
      return response.status(404).json({ error: "CD not found" });
    }

    response.json(deletedCd);

  } catch (err) {
    response.status(500).json({ error: "Error deleting CD" });
  }
});

// ============================
//  Mongoose Setup
// ============================

mongoose  // added extra protection against cluster write issues
  .connect("mongodb+srv://LongBottomLeaf_db_user:dlpXgqGXw5yO4w3l@cluster0.dwadnmh.mongodb.net/CDCollection?retryWrites=true&w=majority&appName=Cluster0", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Connected to MongoDB"))
  .catch((error) => {
    console.error("MongoDB Connection Error!", error);
    mongoose.connection.close();
  });

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
