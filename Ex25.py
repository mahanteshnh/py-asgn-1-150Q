def is_group_number(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False


print(is_group_number([1, 5, 8, 3], 3))
print(is_group_number([2, 4, 5], -1))
