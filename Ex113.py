def check_number():
    try:
        numbers = float(input("Enter a number: "))
        print("Input number:", numbers)
    except ValueError:
        print("Error: Invalid input. Please enter the valid number.")


# Example usage
check_number()
