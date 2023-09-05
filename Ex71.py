'''from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time


#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'


#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))'''

import os
import datetime


def get_directory_listing_sorted_by_creation_date(directory):
    # Get the list of files and directories
    items = os.listdir(directory)

    # Create a list of (file/directory, creation time) tuples
    items_with_creation_time = []
    for item in items:
        item_path = os.path.join(directory, item)
        creation_time = os.path.getctime(item_path)
        items_with_creation_time.append((item, creation_time))

    # Sort the list by creation time
    sorted_items = sorted(items_with_creation_time, key=lambda x: x[1])

    # Return the sorted list
    return sorted_items

# Specify the directory to get the listing
directory_path = input("Enter the directory path: ")

# Call the function to get the sorted directory listing
sorted_listing = get_directory_listing_sorted_by_creation_date(directory_path)

# Print the sorted listing
for item in sorted_listing:
    item_name = item[0]
    creation_time = datetime.datetime.fromtimestamp(item[1])
    print("Item:", item_name, "Creation Time:", creation_time)


for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))

    