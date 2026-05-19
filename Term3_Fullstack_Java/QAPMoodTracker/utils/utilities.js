/**
 * Calculates the number of consecutive positive mood entries,
 * starting from the most recent and going backwards.
 * A positive mood is either "Happy" or "Excited".
 * 
 * @param {Array} moodHistory - An array of mood entry objects {mood: string, date: string}.
 * @returns {number} The count of consecutive positive moods.
 */
function getStreak(moodHistory) {
  if (!moodHistory.length) return 0;
  let streak = 0;

  for (let i = moodHistory.length - 1; i >= 0; i--) {
    const mood = moodHistory[i].mood.toLowerCase();
    if (mood === 'happy' || mood === 'excited') {
      streak++;
    } else {
      break;
    }
  }

  return streak;
}

module.exports = { getStreak };
