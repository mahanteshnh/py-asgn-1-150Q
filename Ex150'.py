def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                product = nums[i] * nums[j]
                if product & 1:
                    return True
    return False


dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [2, 4, 6, 8, 10]
dt4 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))
print(dt4, odd_product(dt4))



'''def distinct_odd_product_exists(sequence):
    odd_numbers = set()
    for num in sequence:
        if num % 2 != 0:
            if num in odd_numbers:
                return True
            odd_numbers.add(num)
    return False


# Test the function
sequence1 = [1, 2, 3, 4, 5]
sequence2 = [2, 4, 6, 8, 10]
sequence3 = [1, 3, 5, 7, 9]

print(distinct_odd_product_exists(sequence1))  # True
print(distinct_odd_product_exists(sequence2))  # False
print(distinct_odd_product_exists(sequence3))  # False'''


