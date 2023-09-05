def add_numbers(m, s):
    if not (isinstance(m, int) and isinstance(s, int)):
        return "Input Must be Integers!"
    return m + s


print(add_numbers(10, 20))
print(add_numbers(10, 20.3))
print(add_numbers('5', 6))
print(add_numbers('5', '5'))

