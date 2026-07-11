##Task 1: Celcius to Fahrenheit
#Input in Celcius
celcius_input = input("Please input temperature in Celcius: ")
#Conver to int and calculate temperature
fahrenheit_result = (int(celcius_input) *9/5) + 32
#Print result
print(f"{celcius_input} degree in Celcius is {fahrenheit_result} degree in Fahrenheit")

##Task 2: Print name in all caps and count how many characters
#Input
name_input = input("Input your name: ")
#Print name and total character
print(f"The name {name_input.upper()} has {len(name_input)} characters")

##Task 3: Boolean age. Adult or not
#Input
age_input = int(input("Input your age: "))
#Print True/False
isAdult = age_input >= 18
print(f"{isAdult} you are an adult") if (age_input > 18) else print(f"{isAdult} you are not an adult yet")

##Task 4: Scoring
#Input
score = int(input("Input your score: "))
#Print True/False
if score >= 80:
    if score > 100:
        print("Not a valid score")
    else:
        print("Exellent! You got A!")
elif score >= 70:
    print("Keep up the good work! You got B!")
elif score >= 60:
    print("It's C!")
else:
    print("FAIL")

##Task 5: Combining task 1-4
#Input
hours_worked = float(input("Input hours worked: "))
if hours_worked > 40:
    pay = (20000*40)+(1.5*20000*(hours_worked-40))
    print(f"Your pay is Rp{pay}")
else:
    pay = 20000*hours_worked
    print(f"Your pay is Rp{pay}")