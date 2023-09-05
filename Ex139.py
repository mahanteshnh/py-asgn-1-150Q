import re


def validate_ip_address(ip_address):
    # RE Expression pattern to match an Ip Address
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # Match the IP Address Pattern
    if re.match(pattern, ip_address):
        return True
    else:
        return False


# Example Usage
input_address = input("Enter an Ip Address: ")
is_valid = validate_ip_address(input_address)

if is_valid:
    print("Valid Ip Address")
else:
    print("Invalid Ip Address")



