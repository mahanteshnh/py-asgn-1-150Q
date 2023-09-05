'''n = "246.4765"
print(float(n))
print(int(float(n)))'''


def test(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


print(test('12'))
print(test('123.23'))

