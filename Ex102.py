import subprocess


def get_command_output(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    return output


# Command to execute
command = 'ls -l'

# Get command output
output = get_command_output(command)
print("Command output:")
print(output)
