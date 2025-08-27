# try except operation in python

try:
    # code that may raise an exception
    result = 10 / 0
except Exception as e:
    # code to handle the exception
    print(f"Error: {e}")
finally:
    # code that will run no matter what
    print("Execution completed.")
    
#################################################
while True:
    try:
        user_input:str = input("Enter a number: ")
        print(f'10 / {user_input} = {10/float(user_input)}')
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Execution completed.")
