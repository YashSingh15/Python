"""
A rudimentary day scheduler that you run as soon as you wake up. Based on the time remaining until 11:30 pm, the program outputs the number of study sessions
you can pull off, with the constraint that there must be 1 CP and 1 Dev session.

A session is defined as 1 hour of study + 30 min of break. So that makes a maximum of 9 sessions physically possible (assuming you sleep 8 hours and 
set aside 2.5 hours for everything else like lunch, dinner, social media).

The goal is to get college subjects out of the way first, and then do CP and Dev sessions alternatively, and keep increasing the number of sessions as you
finish up with more and more college courses through the semester.
"""

from datetime import datetime
from math import floor

# subjects are arranged priority-wise. If time permits, all 7 can be done
  
subjects = {1: "Analog and Digital Systems", 2: "Buggy", 3: "Network Theory", 4: "Computer Networks", 5: "Discrete Mathematics",
            6: "Data Structures and Algorithms", 7: "Humanities"}

current_time = datetime.now()

hours_remaining = 23 - current_time.hour
minutes_remaining = 30 - current_time.minute

if minutes_remaining < 0:
    hours_remaining -= 1
    minutes_remaining += 60

total_time_remaining = hours_remaining * 60 + minutes_remaining  # in minutes

print(f"Time remaining: {hours_remaining}:{minutes_remaining}")

sessions_possible = floor((total_time_remaining - 150) / 90)

if total_time_remaining >= 14.5 * 60:
    sessions_possible = ceil((total_time_remaining - 150) / 90)  # to handle the corner case of going forward
    # with 9 sessions even if you wake up 10 minutes later and hence have slightly less than 16 hours
    # remaining until 11:30 pm

if total_time_remaining >= 13.5 * 60:
    sessions_possible = 9

if sessions_possible < 0:
    sessions_possible = 0

print(f"Number of sessions possible: {sessions_possible}")

print("")
print("Today's Autopilot Routine:\n")

total_subjects = len(subjects)
subjects_possible = min(sessions_possible - 2, len(subjects))

if subjects_possible < 0:
    subjects_possible = 0

for i in range(1, subjects_possible + 1):
    print(subjects[i])

remaining_sessions = sessions_possible - subjects_possible

CP = 0
Dev = 0
while remaining_sessions > 0:
    print("CP")
    CP += 1
    remaining_sessions -= 1
    if remaining_sessions == 0:
        break

    print("Dev")
    Dev += 1
    remaining_sessions -= 1
    if remaining_sessions == 0:
        break
