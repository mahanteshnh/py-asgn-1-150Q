str = 'a123'
#str = '123'
try:
    i = float(str)
    print(i)
except (ValueError, TypeError):
    print(str)
    print('\nNot numeric')
print()
