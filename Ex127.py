'''def check_64bit_integer(num):
    min_val = -(2**63)  # Minimum value for a 64-bit signed integer
    max_val = (2**63)   # Maximum value for a 64-bit signed integer

    if min_val <= num <= max_val:
        return True
    else:
        return False


# Test Cases
integer1 = 12345
print(integer1, "Fits in 64 bits:", check_64bit_integer(integer1))

integer2 = 2**64
print(integer2, "Fits in 64 bits:", check_64bit_integer(integer2))

integer3 = -2**63 - 1
print(integer3, "Fits in 64 bits:", check_64bit_integer(integer3))'''


int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())


