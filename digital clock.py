import tkinter as tk
from tkinter import messagebox
import time

# Global variables for the stopwatch
running = False
counter = 0

# Function to update the clock
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Function to set the alarm
def set_alarm():
    hour = hour_entry.get()
    minute = minute_entry.get()
    second = second_entry.get()

    # Validate hour, minute, and second inputs
    if not (hour.isdigit() and minute.isdigit() and second.isdigit()):
        messagebox.showwarning("Invalid Input", "Please enter numeric values for the alarm time.")
        return

    hour, minute, second = int(hour), int(minute), int(second)
    if not (0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60):
        messagebox.showwarning("Invalid Input", "Please enter a valid time (HH: 0-23, MM: 0-59, SS: 0-59).")
        return

    alarm_time = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    check_alarm(alarm_time)

# Function to check the alarm
def check_alarm(alarm_time):
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        messagebox.showinfo("Alarm", "Time to wake up!")
    else:
        root.after(1000, lambda: check_alarm(alarm_time))

# Functions for the stopwatch
def start_stopwatch():
    global running
    if not running:
        running = True
        update_stopwatch()

def stop_stopwatch():
    global running
    running = False

def reset_stopwatch():
    global counter, running
    running = False
    counter = 0
    stopwatch_label.config(text='00:00:00')

def update_stopwatch():
    if running:
        global counter
        counter += 1
        minutes, seconds = divmod(counter, 60)
        hours, minutes = divmod(minutes, 60)
        stopwatch_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        stopwatch_label.config(text=stopwatch_time)
        stopwatch_label.after(1000, update_stopwatch)

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

# Create the main window
root = tk.Tk()
root.title("3-in-1 Digital Clock")
root.geometry("260x200")

# Create a container frame to hold all sections
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Create frames for Clock, Alarm, and Stopwatch
clock_frame = tk.Frame(container)
alarm_frame = tk.Frame(container)
stopwatch_frame = tk.Frame(container)

for frame in (clock_frame, alarm_frame, stopwatch_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Create the clock section
clock_label = tk.Label(clock_frame, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack(anchor='center', pady=20)
update_clock()

# Create the alarm section
alarm_label = tk.Label(alarm_frame, text="Set Alarm:", font=("Helvetica", 14))
alarm_label.pack(pady=10)

time_frame = tk.Frame(alarm_frame)
time_frame.pack(pady=10)

hour_entry = tk.Entry(time_frame, font=("Helvetica", 14), width=3)
hour_entry.pack(side=tk.LEFT)
hour_label = tk.Label(time_frame, text=":", font=("Helvetica", 14))
hour_label.pack(side=tk.LEFT)

minute_entry = tk.Entry(time_frame, font=("Helvetica", 14), width=3)
minute_entry.pack(side=tk.LEFT)
minute_label = tk.Label(time_frame, text=":", font=("Helvetica", 14))
minute_label.pack(side=tk.LEFT)

second_entry = tk.Entry(time_frame, font=("Helvetica", 14), width=3)
second_entry.pack(side=tk.LEFT)

set_alarm_button = tk.Button(alarm_frame, text="Set Alarm", command=set_alarm, font=("Helvetica", 14))
set_alarm_button.pack(pady=10)

# Create the stopwatch section
stopwatch_label = tk.Label(stopwatch_frame, text="00:00:00", font=("Helvetica", 48), bg="black", fg="white")
stopwatch_label.pack(anchor='center', pady=20)

stopwatch_buttons_frame = tk.Frame(stopwatch_frame)
stopwatch_buttons_frame.pack(pady=10)

start_button = tk.Button(stopwatch_buttons_frame, text="Start", command=start_stopwatch, font=("Helvetica", 14))
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(stopwatch_buttons_frame, text="Stop", command=stop_stopwatch, font=("Helvetica", 14))
stop_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(stopwatch_buttons_frame, text="Reset", command=reset_stopwatch, font=("Helvetica", 14))
reset_button.pack(side=tk.LEFT, padx=5)

# Create navigation buttons
nav_frame = tk.Frame(root)
nav_frame.pack(side="top", fill="x")

clock_button = tk.Button(nav_frame, text="Clock", command=lambda: show_frame(clock_frame))
clock_button.pack(side="left", fill="x", expand=True)

alarm_button = tk.Button(nav_frame, text="Alarm", command=lambda: show_frame(alarm_frame))
alarm_button.pack(side="left", fill="x", expand=True)

stopwatch_button = tk.Button(nav_frame, text="Stopwatch", command=lambda: show_frame(stopwatch_frame))
stopwatch_button.pack(side="left", fill="x", expand=True)

# Show the initial frame
show_frame(clock_frame)

# Run the main event loop
root.mainloop()
