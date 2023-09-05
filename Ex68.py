def sum_of_digits(number):
    sum = 0
    while number != 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum


# Test the function
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits:", result)
