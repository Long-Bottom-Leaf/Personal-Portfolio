# Sorter function for workouts

def sort_workouts_by_date(workouts, newest_first=True):
    return sorted(
        workouts,
        key=lambda workout : workout.workout_date,
        reverse=newest_first
    )
