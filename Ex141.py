'''decimal_number1 = 30
decimal_number2 = 4

hexadecimal1 = hex(decimal_number1)[2:1]  # Remove the '0x' prefix from the hex string
hexadecimal2 = hex(decimal_number2)[2:]  # Remove the '0x' prefix from the hex string

print("Hexadecimal Representation of ", decimal_number1, ":", hexadecimal1)
print("Hexadecimal Representation of ", decimal_number2, ":", hexadecimal2)'''

'''decimal_number1 = 30
decimal_number2 = 4

hexadecimal1 = hex(decimal_number1)[2:]  # Remove the '0x' prefix from the hex string
hexadecimal2 = hex(decimal_number2)[2:]  # Remove the '0x' prefix from the hex string

# Pad with leading zeros if needed
hexadecimal1 = hexadecimal1.zfill(2)
hexadecimal2 = hexadecimal2.zfill(2)

print("Hexadecimal representation of", decimal_number1, ":", hexadecimal1)
print("Hexadecimal representation of", decimal_number2, ":", hexadecimal2)'''

'''x = 1256
print(format(x, '02x'))'''


'''def dechimal_to_Hex(n):
    x = (n % 16)
    ch = ""
    if x < 10:
        ch = x
    if x == 10:
        ch = "A"
    if x == 11:
        ch = "B"
    if x == 12:
        ch = "C"
    if x == 13:
        ch = "D"
    if x == 14:
        ch = "E"
    if x == 15:
        ch = "F"
    if n - x != 0:
        return dechimal_to_Hex(n // 16) + str(ch)
    else:
        return str(ch)


dechimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125, 1256]
print("Dechimal numbers:")
print(dechimal_nums)
print("\nHexadechimal numbers of the said dechimal numbers:")
print([dechimal_to_Hex(x) for x in dechimal_nums])'''


def decimal_to_Hex(decimal_nums):
    digits = "0123456789ABCDEF"
    x = (decimal_nums % 16)
    rest_part = decimal_nums // 16
    if rest_part == 0:
        return digits[x]
    return decimal_to_Hex(rest_part) + digits[x]


decimal_nums = [0, 15, 1125]
print("decimal_nums")
print(decimal_nums)
print("\n Hexadecimal numbers of the said decimal number: ")
print([decimal_to_Hex(x) for x in decimal_nums])

