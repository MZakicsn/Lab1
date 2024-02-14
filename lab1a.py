#!/usr/bin/env python3

# Prompt the user for "Name: "
name = input('Name: ')

# Prompt the user for "Age, accept only integers"
try:
    age = int(input('Age: '))
except ValueError:
    print("Please enter an integer for age.")
    exit(1)  # Exit the program if the input is not an integer

# Print the output
print(f"Hi {name}, nice to meet you. You are {age} years old.")