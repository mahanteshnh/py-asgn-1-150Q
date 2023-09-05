def add_zeros(string, total_length):
    return string.rjust(total_length, '0').ljust(total_length * 2, '0')


# test case
string = "123"
padding_string = add_zeros(string, 2)
print("Padding String:", padding_string)

