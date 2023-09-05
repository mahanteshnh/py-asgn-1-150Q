def round_float(number, decimal_places):
    rounded_number = round(number, decimal_places)
    return rounded_number


# Example usage
float_number = 3.14159
decimal_places = 2


rounded_value = round_float(float_number, decimal_places)
print("Rounded Values: ", rounded_value)
