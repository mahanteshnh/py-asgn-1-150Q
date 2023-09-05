import os


def divide_path_by_extension(path):
    filename, extension = os.path.splitext(path)
    return filename, extension


# Example usage
path = "C:\\Users\\dell pc\\Desktop\\Python\\A.txt"
filename, extension = divide_path_by_extension(path)
print("Filename: ", filename)
print("Extension: ", extension)


