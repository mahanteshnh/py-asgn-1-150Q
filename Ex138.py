def convert_boolean_to_integer(boolean_value):
    if boolean_value:
        return 1
    else:
        return 0


# Example Usage
value1 = True
value2 = False

converted_value1 = convert_boolean_to_integer(value1)
converted_value2 = convert_boolean_to_integer(value2)

print("Converted value1: ", converted_value1)
print("Converted value2: ", converted_value2)


'''x = 'true'
x = int(x == 'true')
print(x)

x = 'abcd'
x = int(x == 'abcd')
print(x)

m = 1.1
m = int(m == 'true')
print(m)

n = 2.2
n = int(n == 2.2)
print(n)'''

