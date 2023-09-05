def split_string_variables(string):
    # Split the string into individual elements
    elements = string.split()

    # Create variables dynamically
    for i, element in enumerate(elements):
        # Generate variable names as var1, var2, var3, ...
        variable_name = "var" + str(i + 1)
        globals()[variable_name] = element

    # Return the variables as a dictionary
    variables = {variable_name: globals()[variable_name] for variable_name in globals() if variable_name.startswith("var")}
    return variables


# Example usage
input_string = input("Enter a string of elements separated by spaces: ")
result = split_string_variables(input_string)
print(result)





