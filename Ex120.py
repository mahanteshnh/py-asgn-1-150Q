def format_string(string, max_length):
    if len(string) > max_length:
        formatted_string = string[:max_length] + "..."
    else:
        formatted_string = string
    return formatted_string


# Example usage
input_string = "This is a long"
max_length = 20

formatted_string = format_string(input_string, max_length)
print("Formatted String: ", formatted_string)

        