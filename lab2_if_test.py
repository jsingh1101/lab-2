if False:
    print('This first print statement will never run')
    print('This second print statement will also not run')
print('This print statement will run')
password = input('Please enter a secret password: ')
if password == 'P@ssw0rd':
    print('You have successfully used the right password')
import sys

# Print the number of command-line arguments
print(len(sys.argv))

# Check if the number of arguments (including script name) is not 10
if len(sys.argv) != 10:
    print('You do not have 10 arguments')
    sys.exit()  # Exit the script if condition is not met
