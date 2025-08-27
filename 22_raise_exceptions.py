# try except operation in python
import sys


def check_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 40:
        print("You are old enough.")
    elif age < 18:
        raise PermissionError("You must be at least 18 years old.")
    else:
        print("Access granted.")

age = 25
try:
    check_age(age) 
except ValueError as e:
    print(f"ValueError: {e}")
except PermissionError as e:
    print(f"PermissionError: {e}")
finally:
    print("Execution completed.")
