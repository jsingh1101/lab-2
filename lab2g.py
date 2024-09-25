#!/usr/bin/env python3
# Author: Jashanpreet Singh
# Author ID: jsingh1101
# Date Created: 2024/09/25

import sys

# Check the number of arguments
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Get timer value from the first argument
else:
    timer = 3  # Default value if no argument is provided

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")
