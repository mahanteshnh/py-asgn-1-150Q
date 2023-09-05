'''num = [2, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()'''


'''def test(nums, n):
   return all(x > n for x in nums)


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list numbers:")
print(nums)
n = 12
print("\nCheck whether all numbers of the said list greater than", n)
print(test(nums, n))
n = 5
print("\nCheck whether all numbers of the said list greater than", n)
print(test(nums, n))'''


def all_numbers_greater_than(numbers, threshold):
   return all(number > threshold for number in numbers)


# Example usage
number_list = [10, 20, 30, 40, 50]
threshold_value = 160

if all_numbers_greater_than(number_list, threshold_value):
   print("All numbers are greater than", threshold_value)
else:
   print("Some numbers are not greater than", threshold_value)

