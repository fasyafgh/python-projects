#Import library
from datetime import datetime

#Create data
attendance = {
    "Andi" : "07:40",
    "Budi" : "07:00",
    "Citra" : "06:59",
    "Dedi" : "07:01",
    "Eri" : "06:40"
}

#Declare format & variable
fmt = "%H:%M"
max_time = datetime.strptime("07:00",fmt)

late_employee = []

#Loop through values
for name, clock_in in attendance.items():
    if datetime.strptime(clock_in,fmt) > max_time:
        print(f"{name} is late")
        late_employee.append(name)

print(f"The person who is/are late: {late_employee}")