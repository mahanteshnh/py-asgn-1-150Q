def test_number(m, n):
    if m == n or abs(m - n) == 5 or (m + n) == 5:
        return True
    else:
        return False


print(test_number(7, 2))
print(test_number(3, 2))
print(test_number(2, 2))
