'''import sys
print("This is the name/path of the script:"), sys.argv[0]
print("Number of Arguments: ", len(sys.argv))
print("Argument list:", str(sys.argv))'''

import sys

# Name of the script
script_name = sys.argv[0]

# Number of arguments
num_arguments = len(sys.argv) - 1

# Arguments passed to the script
arguments = sys.argv[1:]

# Print the information
print("Script name:", script_name)
print("Number of arguments:", num_arguments)
print("Arguments:", arguments)
