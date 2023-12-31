
# Create the login/register window
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Import user-defined modules
import user_management
import fitness_tracker
import alarm

# Main Application Window
root = tk.Tk()
root.title("Fitness Tracker Pro")

# Global Variables
current_user = None
exercise_reminder = None
alarm_active = False
alarm_seconds = 0

# Function to show a message dialog
def show_message(title, message):
    messagebox.showinfo(title, message)

# Function to create a new user
def register_user():
    # Validate user input
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get()

    if not name or not age or not gender or not username or not password:
        show_message("Error", "Please fill in all fields.")
        return

    try:
        age = int(age)
    except ValueError:
        show_message("Error", "Age must be a number.")
        return

    if not user_management.is_valid_username(username):
        show_message("Error", "Invalid username. Please use only alphanumeric characters.")
        return

    if not user_management.is_valid_password(password):
        show_message("Error", "Invalid password. It must have at least 8 characters.")
        return

    # Code to handle user registration
    # Implement further validation and store user data

    show_message("Registration", "User registration successful!")

# Function to validate user login
def login_user():
    # Validate user input
    username = username_entry.get().strip()
    password = password_entry.get()

    if not username or not password:
        show_message("Error", "Please enter a username and password.")
        return

    if not user_management.is_valid_username(username):
        show_message("Error", "Invalid username. Please use only alphanumeric characters.")
        return

    # Code to handle user login
    # Implement further validation and check credentials

    global current_user
    current_user = username

    if current_user:
        show_message("Login", "User login successful!")
        set_reminder()
    else:
        show_message("Login", "Invalid username or password.")

# Function to set exercise reminder
def set_reminder():
    global exercise_reminder

    # Check if a reminder is already set
    if exercise_reminder:
        root.after_cancel(exercise_reminder)

    # Get the current time and set the reminder time
    current_time = datetime.now()
    reminder_time = current_time.replace(hour=8, minute=0, second=0, microsecond=0)

    # Calculate the time difference for the first reminder
    time_difference = reminder_time - current_time

    # If the reminder time has already passed, set the reminder for the next day
    if time_difference.total_seconds() < 0:
        reminder_time += timedelta(days=1)
        time_difference = reminder_time - current_time

    # Schedule the exercise reminder
    exercise_reminder = root.after(int(time_difference.total_seconds() * 1000), show_reminder)

# Function to show the exercise reminder
def show_reminder():
    show_message("Exercise Reminder", "It's time to exercise!")

# Function to open the settings window
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    # Activity Types Options
    activity_types = ["Workout", "Run", "Cycling", "Swimming"]

    # Create activity type label and option menu
    activity_type_label = tk.Label(settings_window, text="Activity Type:", font=("Arial", 12))
    activity_type_label.pack(pady=5)

    activity_type_var = tk.StringVar(settings_window)
    activity_type_var.set(activity_types[0])  # Set initial value

    activity_type_option = tk.OptionMenu(settings_window, activity_type_var, *activity_types)
    activity_type_option.pack(pady=5)

    # Duration Units Options
    duration_units = ["Minutes", "Hours"]

    # Create duration units label and option menu
    duration_units_label = tk.Label(settings_window, text="Duration Units:", font=("Arial", 12))
    duration_units_label.pack(pady=5)

    duration_units_var = tk.StringVar(settings_window)
    duration_units_var.set(duration_units[0])  # Set initial value

    duration_units_option = tk.OptionMenu(settings_window, duration_units_var, *duration_units)
    duration_units_option.pack(pady=5)

    # Distance Units Options
    distance_units = ["Miles", "Kilometers"]

    # Create distance units label and option menu
    distance_units_label = tk.Label(settings_window, text="Distance Units:", font=("Arial", 12))
    distance_units_label.pack(pady=5)

    distance_units_var = tk.StringVar(settings_window)
    distance_units_var.set(distance_units[0])  # Set initial value

    distance_units_option = tk.OptionMenu(settings_window, distance_units_var, *distance_units)
    distance_units_option.pack(pady=5)

# Function to start the alarm
def start_alarm():
    global alarm_active, alarm_seconds
    if not alarm_active:
        try:
            alarm_minutes = int(alarm_minutes_entry.get().strip())
            alarm_seconds = int(alarm_seconds_entry.get().strip())
            if not alarm.is_valid_time(alarm_minutes, alarm_seconds):
                show_message("Error", "Invalid alarm time. Minutes and seconds must be positive integers.")
                return
        except ValueError:
            show_message("Error", "Alarm minutes and seconds must be integers.")
            return

        alarm_seconds_total = alarm_minutes * 60 + alarm_seconds
        if alarm_seconds_total > 0:
            alarm_active = True
            alarm.start_alarm(alarm_minutes, alarm_seconds)
        else:
            show_message("Error", "Alarm minutes and seconds must be greater than zero.")

# Function to update the alarm countdown label
def update_alarm_label(time_left):
    alarm_label.config(text="Time Left: {:02d}:{:02d}".format(time_left // 60, time_left % 60))

# Create the login/register window
login_register_frame = tk.Frame(root, bg="#f2f2f2")
login_register_frame.pack(pady=20)

logo_label = tk.Label(login_register_frame, text="Fitness Tracker Pro", font=("Arial", 24, "bold"), fg="#333")
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

username_label = tk.Label(login_register_frame, text="Username:", font=("Arial", 12))
username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(login_register_frame, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = tk.Label(login_register_frame, text="Password:", font=("Arial", 12))
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(login_register_frame, show="*", font=("Arial", 12))
password_entry.grid(row=2, column=1, padx=10, pady=5)

name_label = tk.Label(login_register_frame, text="Name:", font=("Arial", 12))
name_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(login_register_frame, font=("Arial", 12))
name_entry.grid(row=3, column=1, padx=10, pady=5)

age_label = tk.Label(login_register_frame, text="Age:", font=("Arial", 12))
age_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

age_entry = tk.Entry(login_register_frame, font=("Arial", 12))
age_entry.grid(row=4, column=1, padx=10, pady=5)

gender_label = tk.Label(login_register_frame, text="Gender:", font=("Arial", 12))
gender_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

gender_entry = tk.Entry(login_register_frame, font=("Arial", 12))
gender_entry.grid(row=5, column=1, padx=10, pady=5)

register_btn = tk.Button(login_register_frame, text="Register", command=register_user, font=("Arial", 12), fg="#fff", bg="#4caf50")
register_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="we")

login_btn = tk.Button(login_register_frame, text="Login", command=login_user, font=("Arial", 12), fg="#fff", bg="#2196f3")
login_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a settings menu
settings_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Open Settings", command=open_settings)

# Create a fitness tracking frame
fitness_frame = tk.Frame(root, bg="#f2f2f2")
fitness_frame.pack(pady=20)

fitness_label = tk.Label(fitness_frame, text="Fitness Tracking", font=("Arial", 18), fg="#333", bg="#f2f2f2")
fitness_label.grid(row=0, column=0, columnspan=2, pady=10)

activity_type_label = tk.Label(fitness_frame, text="Activity Type:", font=("Arial", 12), bg="#f2f2f2")
activity_type_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

activity_type_var = tk.StringVar(root)
activity_type_var.set("")  # Set initial value

activity_type_option = tk.OptionMenu(fitness_frame, activity_type_var, "Workout", "Run", "Cycling", "Swimming")
activity_type_option.grid(row=1, column=1, padx=10, pady=5)

duration_label = tk.Label(fitness_frame, text="Duration (minutes):", font=("Arial", 12), bg="#f2f2f2")
duration_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

duration_entry = tk.Entry(fitness_frame, font=("Arial", 12))
duration_entry.grid(row=2, column=1, padx=10, pady=5)

distance_label = tk.Label(fitness_frame, text="Distance (miles):", font=("Arial", 12), bg="#f2f2f2")
distance_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

distance_entry = tk.Entry(fitness_frame, font=("Arial", 12))
distance_entry.grid(row=3, column=1, padx=10, pady=5)

save_btn = tk.Button(fitness_frame, text="Save", command=lambda: save_fitness_entry(activity_type_var.get(), duration_entry.get(), distance_entry.get()), font=("Arial", 12), fg="#fff", bg="#ff9800")
save_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Create an alarm frame
alarm_frame = tk.Frame(root, bg="#f2f2f2")
alarm_frame.pack(pady=20)

alarm_label = tk.Label(alarm_frame, text="Set Alarm", font=("Arial", 18), fg="#333", bg="#f2f2f2")
alarm_label.grid(row=0, column=0, columnspan=2, pady=10)

alarm_minutes_label = tk.Label(alarm_frame, text="Minutes:", font=("Arial", 12), bg="#f2f2f2")
alarm_minutes_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

alarm_minutes_entry = tk.Entry(alarm_frame, font=("Arial", 12))
alarm_minutes_entry.grid(row=1, column=1, padx=10, pady=5)

alarm_seconds_label = tk.Label(alarm_frame, text="Seconds:", font=("Arial", 12), bg="#f2f2f2")
alarm_seconds_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

alarm_seconds_entry = tk.Entry(alarm_frame, font=("Arial", 12))
alarm_seconds_entry.grid(row=2, column=1, padx=10, pady=5)

start_alarm_btn = tk.Button(alarm_frame, text="Start Alarm", command=start_alarm, font=("Arial", 12), fg="#fff", bg="#f44336")
start_alarm_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

alarm_label = tk.Label(alarm_frame, text="Time Left: 00:00", font=("Arial", 14), bg="#f2f2f2")
alarm_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)


# List to store fitness entries
fitness_entries = []

# Function to save fitness entry
def save_fitness_entry(activity_type, duration, distance):
    # Validate user input
    if not activity_type or not duration or not distance:
        show_message("Error", "Please fill in all fields.")
        return

    try:
        duration = int(duration)
        distance = float(distance)
    except ValueError:
        show_message("Error", "Duration must be an integer and distance must be a number.")
        return

    # Add the fitness entry to the list
    fitness_entry = {
        "activity_type": activity_type,
        "duration": duration,
        "distance": distance
    }
    fitness_entries.append(fitness_entry)

    # Clear the entry fields after saving
    activity_type_var.set("")
    duration_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)

    show_message("Fitness Entry", "Fitness entry saved successfully!")

root.mainloop()


