'''import os
print([f for f in os.listdir('C:\\Users\\dell pc\\Desktop\\Python') if os.path.isfile((os.path.join("C:\\Users\\dell pc\\Desktop\\Python\\A.txt"), f))])'''

import os


def find_files(directory):
    # List all items in the directory
    items = os.listdir(directory)

    # Iterate over the items:
    for item in items:
        item_path = os.path.join(directory, item)

        # check if it is a file
        if os.path.isfile(item_path):
            print("File: ", item_path)
        else:
            print("Skipping directory: ", item_path)


# Specify the directory to search
directory_path = input("Enter the directory path: ")

# Call the function to find files
find_files(directory_path)

