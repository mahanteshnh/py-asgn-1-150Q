def sum_counts(collection):
    count_sum = 0
    for count in collection:
        count_sum += count
    return count_sum


# Test case with List
counts_list = [5, 3, 8, 2]
total_count_list = sum_counts(counts_list)
print("Total count in List: ", total_count_list)

# Test case with Tuple
counts_tuple = (10, 7, 4, 1)
total_count_tuple = sum_counts(counts_tuple)
print("Total count in Tuple: ", total_count_tuple)

