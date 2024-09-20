 # Name: [Devinder Chand]
# Assignment: [Assignment 1 - PROG 12853 – Programming Foundations-Python]
# Program: [Computer Programming-PCPRG]

# [Travel Time Calculator- This is small program  that calculates the estimated hours and minutes for a trip. Morover, This program demands user inputs in terms of miles to be covered and total miles per hour that is speed of the vehicle 
# therefore, The program tells the exact time travel]


print("**********************Travel Time Calculator************************")

# This part will demand the user input for miles and speed  only in integers
 
miles = int(input("Enter miles: "))
mph = int(input("Enter miles per hour: "))

# This part of the code firstly calculates the roughly minutes for a trip to avoid any confusion in float   
total_minutes = miles // mph

# Then, this part calculates the exact hours and minutes with the help of integer division and modulo operator
hours = total_minutes 
minutes = total_minutes % 60

# this is the last part which print above variables
print("Estimated travel time")
print("Hours:", hours)
print("Minutes:", minutes) 