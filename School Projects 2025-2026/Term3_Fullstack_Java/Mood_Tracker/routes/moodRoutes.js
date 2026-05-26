const express = require('express');
const router = express.Router();
const { getStreak } = require('../utils/utilities');

const moodHistory = []; // store all moods

// Home page
router.get('/', (req, res) => {
  const streak = getStreak(moodHistory);
  res.render('index', { streak, hasEntries: moodHistory.length > 0 });
});

// Mood entry form
router.get('/mood', (req, res) => {
  res.render('mood');
});

// Handle mood submission
router.post('/mood', (req, res) => {
  const { mood } = req.body;

  moodHistory.push({
    date: new Date().toDateString(),
    mood
  });

  res.redirect('/summary');
});

// Summary page
router.get('/summary', (req, res) => {
  const streak = getStreak(moodHistory);
  const recent = moodHistory.slice(-5).reverse();
  res.render('summary', { streak, recent });
});

module.exports = router;
module.exports.moodHistory = moodHistory;       // export for testing
