# try except operation in python
import sys


while True:
    user_input: str = input("Enter a number: ")
    if user_input.lower() == "exit":
        sys.exit()
    try:
        # code that may raise an exception
        result: float = 10 / float(user_input)
        print(f"Result: {result}")
    except ValueError:
        # code to handle the exception
        print(f"Error: you cant use {user_input} as a value.")
    except ZeroDivisionError:
        print(f"Error: you cant divide by zero.")
    else:
        # code that will run if no exceptions were raised
        print("Success: No exceptions occurred.")
    finally:
        # code that will run no matter what
        print("Execution completed.")