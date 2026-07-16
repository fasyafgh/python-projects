#Import necessary libraries
from datetime import datetime
import pandas as pd

#Function: converting string to time format
def time_format(initial_time):
    fmt = "%H:%M"
    return datetime.strptime(initial_time,fmt)

#Create attendance data in dictionary
def create_data():
    data = {
        "Name": ["Andi", "Budi", "Citra", "Dedi", "Eri"],
        "Clock-In": ["07:40","07:00","06:59","07:01","06:40"]
    }
    df = pd.DataFrame(data)
    df.to_csv("employee_attendance.csv")


#Read created file
def read_data():
    try:
        data = pd.read_csv("employee_attendance.csv")
        return data
    except FileNotFoundError:
        print("File Not Found")
        return None

#Sorting whether a person is late or not
def isLate(clock_in, max_time):
    if clock_in > max_time:
        return "late"
    elif clock_in == max_time:
        return "on time"
    else:
        return "early"

#Calculate time deviation
def time_deviation(arrival_time, max_time):
    #Condition to sort which time is bigger
    if arrival_time >= max_time:
        return ((arrival_time - max_time).total_seconds()/60)
    else:
        return ((max_time - arrival_time).total_seconds()/60)

    
def attendance_result(data):
    max_time = time_format("07:00")
    late_comer = []
    early_comer = []
    
    #Looping through data dictionary
    for x in data.index:
        #Assign columns in file to variable each
        name = data["Name"].loc[x]
        raw_time = data["Clock-In"].loc[x]

        #Error handling for clock in time
        try:
            clock_in = time_format(raw_time)
        except ValueError:
            print(f"Skipping {name}: '{raw_time}' is not a valid time")
            continue

        status = isLate(clock_in,max_time)
        
       #Print result
        if status == "on time":
            print(f"{name} is {status}")
        else:
            minutes = time_deviation(clock_in,max_time) 
            print(f"{name} is {status} by {minutes:.0f} minutes")
            
        #Assign name to list
        if status == "late":
            late_comer.append(name)
        elif status == "early":
            early_comer.append(name)

    return late_comer, early_comer

# Calling Function
# data = create_data()
data = read_data()
late_comer, early_comer = attendance_result(data)
print(f"The people who come early is/are: {early_comer}")
print(f"The people who come late is/are: {late_comer}")



