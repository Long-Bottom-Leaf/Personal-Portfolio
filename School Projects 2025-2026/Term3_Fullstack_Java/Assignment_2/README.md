[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/6tfAhzay)
# QAP 2 – Daily Mood Tracker

This is the starter repository for **QAP 2 – Daily Mood Tracker**, a web application built with Node.js and Express. The goal is to complete the base code so users can record their mood each day, view their positive streak, and see recent mood history.

For full project details, requirements, and grading criteria, refer to the [assignment sheet](https://menglishca.github.io/keyin-course-notes/fullstack/qaps/qap-2/).

## Due Date

**June 12th, 2025 by 11:59 PM**

## Getting Started

This assignment is distributed via GitHub Classroom. Follow these steps to set up your copy of the project:

1. Open the [assignment link](https://classroom.github.com/a/bqWwgZiZ) and choose your name.
2. Click **“Accept this assignment.”**
3. Clone your new repository:
   ```bash
   git clone <your-new-repo-url>
````

4. Navigate into the project directory and install dependencies:

   ```bash
   cd <your-new-repo-name>
   npm install
   ```
5. Start the application:

   ```bash
   npm start
   ```
6. Run the unit tests:

   ```bash
   npm test
   ```

## Overview

This Express app allows a single user to track their daily mood. Each mood is stored in memory, and a streak of positive days is tracked and displayed.

### Required Pages

* **Home Page**

  * Shows a welcome message
  * Displays current streak or “No entries yet.”
  * Includes a button to add a new mood

* **Mood Entry Page**

  * Lets user select today’s mood (Happy, Sad, Okay, Stressed, Excited)
  * Submit button to log the mood

* **Mood Summary Page**

  * Shows current positive streak (consecutive Happy or Excited days)
  * Lists last 5 mood entries
  * Button to return to the home page

## Development Guidelines

* Use **EJS** for all templating
* Data can be stored using in-memory arrays — no database is required
* Assume only **one user** is using the application
* No session handling is needed

### Core Functionality

* Log moods to an in-memory array
* A mood is considered “positive” if it’s “Happy” or “Excited”
* Implement a `getStreak()` function to return the count of consecutive positive days

### Unit Testing

* Write unit tests to check the correctness of your `getStreak()` function
* Test various cases including positive streaks, mixed moods, and edge cases

## Submission Guidelines

* Ensure the app runs using `npm start`
* Ensure all tests pass with `npm test`
* Push all completed work to your GitHub Classroom repo
* Submit the repository link on Teams under the QAP 2 assignment

Late submissions follow Keyin’s late policy, which can be found [here](https://keyincollege289.sharepoint.com/:b:/s/FullstackJavascript-SD13May.2025-Aug.2025/EQsdYpI0N1RPsETRsktEqmkBTDvs1QzdvJT5cmDCQoSHWw?e=ZT4ph9)

If you need an extension, please reach out **before** the due date.
