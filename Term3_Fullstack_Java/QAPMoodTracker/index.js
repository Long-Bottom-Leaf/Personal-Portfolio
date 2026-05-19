const express = require('express');
const path = require('path');
const moodRoutes = require('./routes/moodRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Mount routes
app.use('/', moodRoutes);

app.listen(PORT, () => {
  console.log(`Mood Tracker running at http://localhost:${PORT}`);
});

module.exports = app; // for testing
