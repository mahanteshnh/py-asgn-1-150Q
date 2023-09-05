def is_variable_defined(variable_name):
    if variable_name in locals() or variable_name in globals():
        return True
    else:
        return False


# Example usage
x = 5
y = 10
result1 = is_variable_defined('x')
result2 = is_variable_defined('y')
result3 = is_variable_defined('z')

print("Is 'x' defined?", result1)
print("Is 'y' defined?", result2)
print("Is 'z' defined?", result3)

