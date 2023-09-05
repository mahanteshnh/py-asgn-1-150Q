from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('C:\\Users\\dell pc\\Desktop\\Python') if
              isfile(join('C:\\Users\\dell pc\\Desktop\\Python', f))]
print(files_list)
