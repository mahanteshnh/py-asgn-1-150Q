def in_numbers(x, y, z):
    sum = x+y+z
    if x == y == z:
        sum = sum * 3
    return sum


print(in_numbers(1, 2, 3))
print(in_numbers(2, 2, 2))
