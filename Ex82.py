'''s = sum([10,20,30])
print("\nSum of the container: ", s)
print()'''

# list container
'''nums = [10, 20, 30]
print("Original container:")
print(nums)
print(type(nums))
print("Sum of all items of the said container:", sum(nums))'''


# Dictionary container


def dict_sum(nums):
    num_sum = 0
    for i in nums:
        num_sum = num_sum + nums[i]
    return num_sum


nums = {'a': 100, 'b': 200, 'c': 300, 'd': 120}
print("Original container:")
print(nums)
print(type(nums))
print("Sum of all items of the said container:", dict_sum(nums))


# set container
nums = {7, 4, 9, 1, 3, 2}
print("The original container")
print(nums)
print(type(nums))
sum_tuple = sum(nums)
print("Sum of all items of the said container:", str(sum_tuple))

# tuple container
nums = (7, 4, 9, 1, 3, 2)
print("The original container")
print(nums)
print(type(nums))
sum_tuple = sum(nums)
print("Sum of all items of the said container:", str(sum_tuple))

