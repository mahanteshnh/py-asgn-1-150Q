import os


def extract_filename(path):
    filename = os.path.basename(path)
    return filename


# Example usage
path = "C:\\Users\\dell pc\\Desktop\\Python\\A.txt"
filename = extract_filename(path)
print("Filename: ", filename)
