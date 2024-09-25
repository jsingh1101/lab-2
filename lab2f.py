#!/usr/bin/env python3
# Author: Jashanpreet Singh
# Author ID: jsingh1101
# Date Created: 2024/09/25


import sys

# Check if an argument is passed, default to 10
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 10  # Default value if no argument is provided

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")
import sys

if len(sys.argv) != 2:  # Adjust this according to how many arguments you expect
    print("Error: This script requires exactly one argument.")
    sys.exit(1)  # Exit with code 1 for error
