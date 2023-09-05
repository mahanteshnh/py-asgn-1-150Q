
'''import os
home_directory = os.path.expanduser("~")
relative_path = os.path.relpath(home_directory)
print("Home Directory: ", relative_path)'''

'''import os.path
home_directory = (os.path.expanduser('~'))
print(home_directory)
relative_path = os.path.relpath(home_directory)
print("Home Directory: ", relative_path)'''

import os.path

home_directory = os.path.expanduser('~')
print(home_directory)
relative_path = os.path.relpath(home_directory)
print(relative_path)
print("Home Directory: ", relative_path)
