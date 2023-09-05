'''soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

word = input("Input the word be hashed: ")

word = word.upper()

coded = word[0]

for a in word[1:len(word)]:
    i = 65 - ord(a)
    coded = coded + str(soundex[i])
print()
print("The coded word is: " + coded)
print()'''

int_num = 112
flt_num = 23.99
text_val = 'Python Exercises'
print("Original integer value:", int_num)
print("Hash value of the said integer value: " + str(hash(int_num)))
print("Original float value:", flt_num)
print("Hash value of the said float value: " + str(hash(flt_num)))
print("Original text:", text_val)
print("Hash value of the said text: " + str(hash(text_val)))

