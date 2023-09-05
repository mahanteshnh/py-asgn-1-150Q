'''my_dict = {"name": "John", "age": 25, "city": "Newyork"}

# Extract single-key value pair
key, value = my_dict.popitem()

# Print the extracted key-value pair
print("Key: ", key)
print("Value: ", value)'''

'''d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)'''


dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
print("Extract specific key, value")
x, y = list(dict.items())[0]
print(x, y)
x, y = list(dict.items())[1]
print(x, y)


