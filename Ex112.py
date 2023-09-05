def remove_first_item(lst):
    if lst:
        lst.pop(0)
    return lst


# Example usage

my_list = [1, 2, 3, 4, 5]
updated_list = remove_first_item(my_list)
print("updated list: ", updated_list)
