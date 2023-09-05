numbers = [45, 30, 60, 17, 90, 75, 105]
divisible_by_fifteen = list(filter(lambda x: x % 15 == 0, numbers))
print("Numbers divisible by fifteen: ", divisible_by_fifteen)
