def check_same_value(*args):
    # get the first value to compare against
    first_value = args[0]

    # Iterate over the remaining value
    for value in args[1:]:
        if value != first_value:
            return False

    return True


# test cases
x = 10
y = 10
z = 10
result = check_same_value(x, y, z)
print("x, y, z  have the same value:", result)

a = "Hello"
b = "World"
c = "Hello"
result = check_same_value(a, b, c)
print("a, b, and c have the same value:", result)

p = 3.14
q = 2.71
r = 3.14
result = check_same_value(p, q, r)
print("p, q, and r have the same value:", result)

