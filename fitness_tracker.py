# fitness_tracker.py

def save_fitness_entry(activity_type, duration, distance):
    # Implement fitness entry saving logic here
    # Validate input and store fitness data
    if not is_valid_duration(duration) or not is_valid_distance(distance):
        raise ValueError("Invalid duration or distance. Both must be positive numbers.")

    # Code to save the fitness entry
    # Implement further validation and data storage
    # For example:
    # fitness_data = {
    #     "activity_type": activity_type,
    #     "duration": float(duration),
    #     "distance": float(distance)
    # }
    # Save fitness_data to a database or file

def is_valid_duration(duration):
    # Function to validate the duration input
    # Implement validation logic here (e.g., positive float)
    try:
        duration = float(duration)
        return duration >= 0
    except ValueError:
        return False

def is_valid_distance(distance):
    # Function to validate the distance input
    # Implement validation logic here (e.g., positive float)
    try:
        distance = float(distance)
        return distance >= 0
    except ValueError:
        return False
