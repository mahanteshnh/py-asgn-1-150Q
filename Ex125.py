'''import collections
num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
print(sum(collections.Counter(num).values()))'''


def sum_counts(collection):
    return sum(collection.values())


# Test case : Dictionary with counts

counts_dict = {"a": 5, "b": 10, "c": 3}
total_count = sum_counts(counts_dict)
print("Total Count:", total_count)

# Test case: List of counts

counts_list = [2, 4, 6, 8, 10]
total_count = sum_counts(counts_list)
print("Total Count:", total_count)

# Test case: Tuple of counts

counts_tuple = (1, 3, 5, 7, 9)
total_count = sum_counts(counts_tuple)
print("Total count:", total_count)



