import glob


def get_file_list(pattern):
    file_list = glob.glob(pattern)
    return file_list


# Example usage
pattern = "C:\\Users\\dell pc\\Desktop\\Python\\*.txt"
file_list = get_file_list(pattern)

# Display the file list

for file_path in file_list:
    print(file_path)
