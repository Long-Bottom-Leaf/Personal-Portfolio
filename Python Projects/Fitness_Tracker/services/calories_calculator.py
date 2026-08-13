# Base calorie numbers

MET_VALUES = {
    "Cycling": {
        "low": 4.0,
        "medium": 6.8,
        "high": 10.0
    },
    "General Cardio": {
        "low": 3.5,
        "medium": 6.0,
        "high": 8.0
    },
    "Running": {
        "low": 6.0,
        "medium": 9.8,
        "high": 11.5
    },
    "Swimming": {
        "low": 5.8,
        "medium": 8.3,
        "high": 10.0
    },
    "Weights": {
        "low": 3.5,
        "medium": 5.0,
        "high": 6.0
    },
    "Other": {
        "low": 3.0,
        "medium": 5.0,
        "high": 7.0
    }
}

def calculate_calories(workout_type, intensity, weight, duration, weight_unit):
    if weight_unit.strip().lower() == 'lbs':
        weight_kg = weight / 2.20462  # Convert pounds to kg
    else:
        weight_kg = weight

    duration_hours = duration / 60

    met = MET_VALUES[workout_type][intensity.strip().lower()]

    calories = met * weight_kg * duration_hours

    return round(calories)
