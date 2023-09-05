import os


def find_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in files or name in dirs:
            return os.path.join(root, name)
    return None


# Example Usage
search_name = 'A.txt'
search_path = "C:\\Users\\dell pc\\Desktop\\Python"

result = find_path(search_name, search_path)
if result:
    print("Path:", result)
else:
    print("File or directory not found.")

