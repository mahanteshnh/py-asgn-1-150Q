def filter_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers


# Example usage
my_list = [1, -2, 3, -4, 5, -6, 7]
positive_numbers = filter_positive_numbers(my_list)
print("Positive numbers:", positive_numbers)
