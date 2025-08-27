"""
This script demonstrates the concept of Python modules.
Modules are files containing Python code (functions, classes, variables) that can be imported and reused.
Below, we use several built-in modules: time, sys, datetime, os, and math.

References:
- https://docs.python.org/3/library/time.html
- https://docs.python.org/3/library/sys.html
- https://docs.python.org/3/library/datetime.html
- https://docs.python.org/3/library/os.html
- https://docs.python.org/3/library/math.html
"""

# Importing built-in modules
import time        # Time-related functions
import sys         # System-specific parameters and functions
import datetime    # Date and time manipulation
import os          # Operating system interfaces
import math        # Mathematical functions

# Using the time module
print("Current time (epoch):", time.time())  # Returns seconds since epoch
time.sleep(1)  # Pauses execution for 1 second

# Using the sys module
print("Python version:", sys.version)
print("Command line arguments:", sys.argv)

# Using the datetime module
now = datetime.datetime.now()
print("Current date and time:", now)
print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Using the os module
print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir('.'))

# Using the math module
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# Custom module example (if you have a file named mymodule.py)
# import mymodule
# mymodule.my_function()

# Summary:
# - Modules help organize code and reuse functionality.
# - Built-in modules provide ready-to-use features.
# - Custom modules can be created for your own code.