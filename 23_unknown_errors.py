def risky_operation():
    raise NotImplementedError

try:
    # Your code that might raise unknown errors
    risky_operation()
except NotImplementedError as nie:
    print(f"NotImplementedError: {nie}")
except Exception as e:
    print(f"An unknown error occurred: {e}")
    print(f"Error type: {type(e).__name__}")
    print("Additional context: This error occurred in the risky_operation function.")
finally:
    print("Execution completed.")
