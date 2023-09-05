def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result


print(concatenate_list_data([2, 3, 'hello', 5, True, 2.3]))
