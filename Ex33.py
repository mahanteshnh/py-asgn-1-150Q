
def sum_3(m, n, o):
    if m == n or n == o or m == o:
        sum = 0
    else:
        sum = m + n + o
    return sum


print(sum_3(2, 1, 4))
print(sum_3(3, 4, 3))


