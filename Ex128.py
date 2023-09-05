
'''str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))'''


def has_lower_letters(string):
    for char in string:
        if char.islower():
            return True
    return False


# Test cases

string1 = "Hello world"
print("Lowercase letter exists:", has_lower_letters(string1))

string2 = "HELLO WORLD"
print("Lowercase letter exists:", has_lower_letters(string2))

string3 = "12345"
print("Lowercase letter exists:", has_lower_letters(string3))

