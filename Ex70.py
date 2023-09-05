import os
os.chdir('c:')
result = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
print('\n'.join(map(str, result)))





'''import glob
import os
files = glob.glob("C:\\Users\\dell pc\\Desktop\\Python\\*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))'''






'''import os
import datetime


def get_file_modified_date(file_path):
    timestamp = os.path.getmtime(file_path)
    modified_date = datetime.datetime.fromtimestamp(timestamp)
    return modified_date


def sort_files_by_date(directory):
    file_list = os.listdir(directory)
    file_paths = [os.path.join(directory, file) for file in file_list]
    sorted_files = sorted(file_paths, key=get_file_modified_date)
    return sorted_files


# Test the function
directory = input("Enter the directory path: ")
sorted_files = sort_files_by_date(directory)

print("Sorted files:")
for file in sorted_files:
    print(file)
'''