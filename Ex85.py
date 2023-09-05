import os
path = "C:\\Users\\dell pc\\Desktop\\Python\\A.txt"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a FileName")
else:
    print("It is a special file (socket, FIFO, device file")
print()
