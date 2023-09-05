def list_count_num4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count


print(list_count_num4([1, 2, 3, 4]))
print(list_count_num4([4, 4, 4]))
