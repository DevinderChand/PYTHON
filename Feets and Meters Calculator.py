# Name: [Devinder Chand]
# Assignment: [Assignment 2 - PROG 12853 – Programming Foundations-Python]
# Program: [Computer Programming-PCPRG]

# [Feet and Meters Calculator- This is small program  that converts feet to meters and vice versa.]


print("**********************Feet and Meters Converter ************************")

# This part displays the conversions menu and hints the user for two options 'a' and 'b' . 

print("Conversions Menu :")
print("a. Feet to Meters")
print("b. Meters to Feet")

# This is the constant which is used further for conversion 
CONSTANT = 0.3048

# This program used condition-controlled loop 
#This is the starting of the program with choice variable 
choice = "y"

# This part of the program starts the while loop and puts the condition on choice variable and automatically converts the user input into  small case y to remove error. 
while choice.lower() == "y" :
    
# This part demands the user input about the 'a' or 'b' option in the conversions menu
    option = input("Select a conversion (a/b): ")

# This the main part of the program which uses multiple alternative decision structure
# Firstly, if the input is 'a' or 'A' then, it ask for the feet in floating point value
    if option.lower() =="a" : 
        feet = float(input("Enter feet :"))
        
# This part describes the formula for the feet to meters and prints the converted meters upto two decimal values 
        converted_meters = feet * CONSTANT
        print ( round (converted_meters,2), " meters " )

# if the input is 'b'or 'B' then, it ask for the meters in floating point value
    elif option.lower() == "b" :
        meters = float(input("Enter meters :"))

# This part describes the formula for the meters to feet  and prints the converted feet upto two decimal values 
        converted_feet = meters / CONSTANT
        print ( round( converted_feet,2) , " feet " )

# if the user enters no valid options except a and b , then the following statement prints
    else:
        print("You did not enter a valid selection.")

# This part again ask the user if they want to perform another conversion and expect the answer in both upper and lower case.
# if answer is 'y' in any case then, the loop continues , otherwise it ends for any alphabets enters
    choice = input("Would you like to perform another conversion ? (y/n) :")

# This is the end of the program and prints the following statement
print("Thanks, bye!") 

    
















































