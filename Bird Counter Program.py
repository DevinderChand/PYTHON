# Name: [Devinder Chand]
# Assignment: [Assignment 3 - PROG 12853 – Programming Foundations-Python]
# Program: [Computer Programming-PCPRG]

# [Bird Counter- This is small program   for birdwatchers that stores a list of birds along with a count of the
# number of times each bird has been spotted ]

# This is initial part  of the program which describes the name and key to exit the program

print("Bird Counter program")

print("Enter 'x' to exit")


# This part of the program create a empty dictionary to store the list of sighted birds
sighted_birds = {}

# This is the main part of the program which ask the user input the name of spotted bird and useswhile loop , if and else statements.
while True:
    bird_name = input("Enter name of bird: ")
    # The while automatically break if user enters 'x'
    if bird_name == 'x':
        break

    # This part capitalizes the bird name 

    bird_name = bird_name.capitalize()

    # This part again ask the user the sighted birdsby adding the elements in dictionary until it ask x to terminate the program
    if bird_name in sighted_birds:
        sighted_birds[bird_name] += 1
    else:
        sighted_birds[bird_name] = 1

# This part of the program sort the sighted birds 
sorted_birds = sorted(sighted_birds.items())


# This is the print statements which print the Name and Count as well as equal to signs .
print("\nName\t\t\tCount")
print("=" * 20 + "\t======")

# This is the last part of the program which uses for loop to create the tabular representation of Name of the bird with its count 

for bird, count in sorted_birds:
    print(bird.ljust(25) + str(count))



