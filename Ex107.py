import os
import time


def get_file_properties(filepath):
    # get the file size
    size = os.path.getsize(filepath)

    # get file creation time
    creation_time = os.path.getctime(filepath)
    formatted_creation_time = time.ctime(creation_time)

    # get file modification time
    modification_time = os.path.getmtime(filepath)
    formatted_modification_time = time.ctime(modification_time)

    # get file access time
    access_time = os.path.getatime(filepath)
    formatted_access_time = time.ctime(access_time)

    # get file permissions
    permissions = oct(os.stat(filepath).st_mode)[-3:]

    # create  dictionary of file properties
    properties = {
        'File Path': filepath,
        'Size': size,
        'Creation Time': formatted_creation_time,
        'Modification Time': formatted_modification_time,
        'Access Time': formatted_access_time,
        'Permissions': permissions
    }

    return properties


# Example usage
file_path = "C:\\Users\\dell pc\\Desktop\\Python\\A.txt"
file_properties = get_file_properties(file_path)

# Display file properties
for key, value in file_properties.items():
    print(f'{key}: {value}')
