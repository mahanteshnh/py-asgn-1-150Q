'''import platform
import os
print("Name of the operating system: ", os.name)
print("\nName of the operating system: ", platform.system())
print("\nVersion of the operating system: ", platform.release())'''

import os
import sys
import platform
import sysconfig
print("os.name                      ", os.name)
print("sys.platform                 ", sys.platform)
print("platform.system()            ", platform.system())
print("sysconfig.get_platform()     ", sysconfig.get_platform())
print("platform.machine()           ", platform.machine())
print("platform.architecture()      ", platform.architecture())

