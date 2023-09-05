amt = 10000
int = 24
year = 1
future_values = amt * ((1 + (0.01*int)) ** year)
print(round(future_values, 2))


simple_interest = (amt * year * int)/100
print(round(simple_interest, 2))
