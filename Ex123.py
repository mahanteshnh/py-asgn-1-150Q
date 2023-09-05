'''import sys
print("Float value information: ", sys.float_info)
print("\nInteger value information: ", sys.int_info)
print("\nMaximum Size of an Integer: ", sys.maxsize)'''

import sys

# Integer values
integers = [10, -5, 100, 0, -50]
largest_integer = sys.maxsize * -1
print(largest_integer)
smallest_integer = sys.maxsize
print(smallest_integer)

for num in integers:
    if num > largest_integer:
        largest_integer = num
    if num < smallest_integer:
        smallest_integer = num

# Long Values
longs = [9223372036854775807, -9223372036854775808, 0]
largest_long = sys.maxsize * -1
print(largest_long)
smallest_long = sys.maxsize
print(smallest_long)
for num in longs:
    if num > largest_long:
        largest_long = num
    if num < smallest_long:
        smallest_long = num

# Float Values

floats = [3.14, -1.23, 100.0, 0.0, -50.5]
largest_float = -sys.float_info.max
print(largest_float)
smallest_float = sys.float_info.max
print(smallest_float)
for num in floats:
    if num > largest_float:
        largest_float = num
    if num < smallest_float:
        smallest_float = num

# output the results

print("Largest Integer: ", largest_integer)
print("Smallest Integer: ", smallest_integer)
print("Largest Long: ", largest_long)
print("Smallest Long: ", smallest_long)
print("Largest Float: ", largest_float)
print("Smallest Float: ", smallest_float)

