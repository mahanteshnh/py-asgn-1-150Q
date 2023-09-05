from functools import reduce
import operator


def compute_product(numbers):
    product = reduce(operator.mul, numbers)
    return product


# Example usage
my_list = [2, 3, 4, 5]
result = compute_product(my_list)
print("Product: ", result)
