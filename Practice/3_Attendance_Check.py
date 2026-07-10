#Import necessary libraries
from datetime import datetime

#Define clock-in time format
fmt = "%H:%M"

#Ask for input
input_arrival = input("Insert employee arrival time: ")

#Define max value for arrival time
max_time = datetime.strptime("07:00",fmt)

#Define variable arrival time
arrival_time = datetime.strptime(input_arrival,fmt)

#Calculate deviation from max_time
minutes_late = (arrival_time-max_time).total_seconds()/60
minutes_early = (max_time-arrival_time).total_seconds()/60

#Condition to sort attendance
if arrival_time>max_time:
    print(f"Late by {minutes_late:.0f} minutes")
elif arrival_time==max_time:
    print("On Time")
else:
    print(f"Late by {minutes_early:.0f} minutes")
