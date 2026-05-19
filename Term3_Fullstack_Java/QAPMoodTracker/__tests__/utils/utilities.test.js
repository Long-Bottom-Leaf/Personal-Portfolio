const { getStreak } = require('../utils/utilities');
    
describe('Tests for mood tracker to make sure it tracks, stores, and displays moods correctly', () => {
  test('Returns 0 for empty array', () => {
    expect(getStreak([])).toBe(0);
  });

  test('Returns full streak of positive moods', () => {
    const moods = [{ mood: 'Happy' }, { mood: 'Excited' }];
    expect(getStreak(moods)).toBe(2);
  });

  test('Stops counting when non-positive mood appears', () => {
    const moods = [{ mood: 'Happy' }, { mood: 'Sad' }, { mood: 'Excited' }];
    expect(getStreak(moods)).toBe(1);
  });

  test('Handles lowercase moods', () => {
    const moods = [{ mood: 'excited' }, { mood: 'happy' }];
    expect(getStreak(moods)).toBe(2);
  });
});
