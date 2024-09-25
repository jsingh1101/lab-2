#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:  # Check if there are exactly 2 additional arguments
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()  # Exit the program if the condition is not met

# Assign arguments to name and age
name = sys.argv[1]
age = sys.argv[2]

# Print the final output message
print(f"Hi {name}, you are {age} years old.")
