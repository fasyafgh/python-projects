#Import necessary libraries
from datetime import datetime

#Function: converting string to time format
def time_format(initial_time):
    fmt = "%H:%M"
    return datetime.strptime(initial_time,fmt)

#Create attendance data in dictionary
def create_data():
    attendance = {
        "Andi" : "07:40",
        "Budi" : "07:00",
        "Citra" : "06:59",
        "Dedi" : "07:01",
        "Eri" : "06:40"
    }
    return attendance

#Sorting whether a person is late or not
def isLate(clock_in, max_time):
    clock_in = time_format(clock_in)
    if clock_in > max_time:
        return "late"
    elif clock_in == max_time:
        return "on time"
    else:
        return "early"

#Calculate time deviation
def time_deviation(arrival_time, max_time):
    dev_time = time_format(arrival_time)
    #Condition to sort which time is bigger
    if dev_time >= max_time:
        return ((dev_time - max_time).total_seconds()/60)
    else:
        return ((max_time - dev_time).total_seconds()/60)
    
def attendance_result(data):
    max_time = time_format("07:00")
    late_comer = []
    early_comer = []
    
    #Looping through data dictionary
    for name, clock_in in data.items():
        status = isLate(clock_in,max_time)
        minutes = time_deviation(clock_in,max_time) 
        print(f"{name} is {status} by {minutes:.0f} minutes")

        #Assign lists content
        if status == "late":
            late_comer.append(name)
        elif status == "early":
            early_comer.append(name)
    
    return late_comer, early_comer

#Calling Function
data = create_data()
late_comer, early_comer = attendance_result(data)
print(f"The people who come early is/are: {early_comer}")
print(f"The people who come late is/are: {late_comer}")
