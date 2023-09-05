import os.path
print(os.path.isfile("C:\\Users\\dell pc\\Desktop\\Python\\A.txt"))
print(os.path.isfile("C:\\Users\\dell pc\\Desktop\\Python\\B.txt"))

print(os.path.exists("C:\\Users\\dell pc\\Desktop\\Python\\A.txt"))
print(os.path.exists("C:\\Users\\dell pc\\Desktop\\Python\\B.txt"))

my_file = open("C:\\Users\\dell pc\\Desktop\\Python\\A.txt")
try:
    my_file.close()
    print("File found")
except FileNotFoundError:
    print("File Not Found")
