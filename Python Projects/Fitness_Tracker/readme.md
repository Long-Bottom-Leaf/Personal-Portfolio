# Fitness Tracker

A command-line fitness tracking application built with Python. The project allows users to create a profile, log workouts, set fitness goals, track progress, calculate calories burned, and export workout history to CSV.

The project was built to practice Python fundamentals, object-oriented programming, modular application design, file handling, data validation, and unit testing.

## Features

### Profile Management

* Create and view a user profile
* Store user weight in kilograms or pounds
* Validate profile information
* Clear profile information with confirmation

### Workout Tracking

* Add workouts with:

  * Workout type
  * Date
  * Duration
  * Intensity
  * Automatically calculated calories
  * Notes
* View workout history
* Sort workouts by newest or oldest
* View workout statistics
* Clear workout history with confirmation

### Workout Summary

The application provides a summary including:

* Total workouts
* Total duration
* Total calories burned
* Average workout duration
* Average calories burned
* Favorite workout type
* Longest workout
* Highest-calorie workout

### Goal Tracking

Users can create weekly goals for:

* Number of workouts
* Total workout duration
* Calories burned
* Specific workout type

The application calculates and displays progress toward each goal as a percentage.

### Data Storage & Export

* Persistent JSON data storage
* Load and save profile, workout, and goal data
* CSV export for workout history
* Automatic creation of required data/export directories
* Error and success messages for file operations

### Input Validation

The application validates:

* Names
* Weight
* Weight units
* Workout types
* Workout duration
* Workout intensity
* Goal values
* Menu choices
* Dates

Invalid input is rejected with appropriate error messages.

## Technologies

* **Python 3**
* **JSON** — persistent application data
* **CSV** — workout history export
* **unittest / pytest** — automated testing
* **Rich** — loading/progress indicators
* **Git & GitHub** — version control

## Project Structure

```text
Fitness-Tracker/
│
├── data/
│   └── fitness_data.json
│
├── exports/
│   └── workout_history.csv
│
├── models/
│   ├── goal.py
│   ├── user_profile.py
│   └── workout.py
│
├── services/
│   ├── actions.py
│   ├── calories_calculator.py
│   ├── csv_exporter.py
│   ├── data_manager.py
│   ├── fitness_tracker.py
│   └── goal_tracker.py
│
├── tests/
│   ├── test_calories_calculator.py
│   ├── test_fitness_tracker.py
│   ├── test_goal_tracker.py
│   ├── test_models.py
│   ├── test_sorter.py
│   └── test_utils.py
│
├── utils/
│   ├── error_messages.py
│   ├── formatters.py
│   ├── input_functions.py
│   ├── loading_bar.py
│   ├── sorter.py
│   ├── success_messages.py
│   └── validators.py
│
├── main.py
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Fitness-Tracker
```

### 2. Install dependencies

If using a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python main.py
```

The application will display the main menu and guide you through the available features.

## Running Tests

The project includes unit tests covering the application's core functionality.

Using pytest:

```bash
pytest
```

Or using Python's built-in unittest discovery:

```bash
python -m unittest discover
```

The tests cover areas including:

* Models
* Validators
* Date formatting
* Workout sorting
* Calorie calculations
* Fitness tracker functionality
* Goal tracking
* Data management

## Data Storage

Application data is stored locally in JSON format:

```text
data/fitness_data.json
```

Workout history can also be exported to:

```text
exports/workout_history.csv
```

The application automatically creates these directories when required.

## What I Practiced

This project was designed as a practical exercise in Python development and helped reinforce:

* Object-oriented programming
* Classes and objects
* Functions and modular design
* Lists and dictionaries
* Exception handling
* File I/O
* JSON serialization/deserialization
* CSV generation
* Input validation
* Date handling
* Sorting
* Data processing
* Unit testing
* Separation of concerns
* CLI application design
* Git/GitHub workflow

## Future Improvements

Possible future improvements include:

* Support for multiple user profiles
* Database storage using SQL
* More advanced workout scheduling
* Additional workout statistics
* Improved CLI interface
* More comprehensive reporting

## Author

**Stephen Fennelly**

This project was created as part of my Python learning and portfolio development.
