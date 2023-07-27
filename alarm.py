# alarm.py

import tkinter as tk
from tkinter import messagebox

alarm_active = False
alarm_seconds = 0

def start_alarm(minutes, seconds, alarm_label, root):
    # Function to start the alarm countdown
    global alarm_active, alarm_seconds
    if not alarm_active:
        try:
            alarm_minutes = int(minutes)
            alarm_seconds = int(seconds)
            if not is_valid_time(alarm_minutes, alarm_seconds):
                messagebox.showerror("Error", "Invalid alarm time. Minutes and seconds must be positive integers.")
                return
        except ValueError:
            messagebox.showerror("Error", "Alarm minutes and seconds must be integers.")
            return

        alarm_seconds_total = alarm_minutes * 60 + alarm_seconds
        if alarm_seconds_total > 0:
            alarm_active = True
            countdown_alarm(alarm_seconds_total, alarm_label, root)
        else:
            messagebox.showerror("Error", "Alarm minutes and seconds must be greater than zero.")

def countdown_alarm(seconds_left, alarm_label, root):
    # Function to handle the alarm countdown
    global alarm_active
    if seconds_left > 0 and alarm_active:
        update_alarm_label(alarm_label, seconds_left)
        root.after(1000, countdown_alarm, seconds_left - 1, alarm_label, root)
    elif seconds_left == 0 and alarm_active:
        update_alarm_label(alarm_label, seconds_left)
        messagebox.showinfo("Alarm", "Time's up!")
        alarm_active = False

def is_valid_time(minutes, seconds):
    # Function to validate the alarm time input
    return minutes >= 0 and seconds >= 0

def update_alarm_label(alarm_label, time_left):
    # Function to update the alarm countdown label
    alarm_label.config(text="Time Left: {:02d}:{:02d}".format(time_left // 60, time_left % 60))
