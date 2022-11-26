# Write a Python program to get the Python version you are using.
# A string containing the version number of the Python interpreter
# plus additional information on the build number and compiler used.
# This string is displayed when the interactive interpreter is started.

import sys
import platform
print("Python version: " + str(sys.version))
print("Version info: " + str(sys.version_info))
print("\nUsing Platform")
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))
