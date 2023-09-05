import os.path
import time
print("Last Modified: %s" % time.ctime(os.path.getmtime("C:\\Users\\dell pc\\Desktop\\Python\\A.txt")))
print("Created: %s" % time.ctime(os.path.getctime("C:\\Users\\dell pc\\Desktop\\Python\\A.txt")))

