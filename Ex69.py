def sort_three_numbers(a, b, c):
    numbers = [a, b, c]
    return tuple(sorted(numbers))


# Test the function
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

sorted_numbers = sort_three_numbers(a, b, c)
print("Sorted numbers:", sorted_numbers)
