# 30_truthy_falsy.py

"""
Python Truthy and Falsy Values 

In Python, every value has an inherent "truthiness" or "falsiness" when evaluated in a boolean context.
This means that values are implicitly converted to `True` or `False` when used in conditional statements
(like `if`, `elif`, `while` loops) or with boolean operators (`and`, `or`, `not`).

Understanding truthy and falsy values is crucial for writing concise and Pythonic code.
"""

# --- 1. Falsy Values --- #
"""
The following values are considered Falsy in Python:
- `None`: The absence of a value.
- `False`: The boolean false value.
- Numeric Zeros: `0` (integer), `0.0` (float), `0j` (complex).
- Empty Sequences: `""` (empty string), `[]` (empty list), `()` (empty tuple).
- Empty Mappings: `{}` (empty dictionary).
- Empty Sets: `set()` (empty set).
- Empty Ranges: `range(0)`.
"""

print("--- Falsy Values Examples ---")

if not None:
    print("None is falsy.")

if not False:
    print("False is falsy.")

if not 0:
    print("Integer 0 is falsy.")

if not 0.0:
    print("Float 0.0 is falsy.")

if not 0j:
    print("Complex 0j is falsy.")

if not "":
    print("Empty string \"\" is falsy.")

if not []:
    print("Empty list [] is falsy.")

if not ():
    print("Empty tuple () is falsy.")

if not {}:
    print("Empty dictionary {} is falsy.")

if not set():
    print("Empty set set() is falsy.")

if not range(0):
    print("Empty range range(0) is falsy.")

print("\n")

# --- 2. Truthy Values --- #
"""
All values that are not explicitly defined as falsy are considered Truthy.
This includes:
- `True`: The boolean true value.
- Any non-zero number: `1`, `-1`, `0.1`, etc.
- Non-empty sequences: `"hello"`, `[1, 2]`, `(1,)`, etc.
- Non-empty mappings: `{"key": "value"}`.
- Non-empty sets: `{1, 2}`.
- Objects (instances of classes) generally evaluate to True unless their `__bool__` or `__len__` method returns False or 0 respectively.
"""

print("--- Truthy Values Examples ---")

if True:
    print("True is truthy.")

if 1:
    print("Integer 1 is truthy.")

if -10:
    print("Negative integer -10 is truthy.")

if 3.14:
    print("Float 3.14 is truthy.")

if "hello":
    print("Non-empty string \"hello\" is truthy.")

if [1, 2, 3]:
    print("Non-empty list [1, 2, 3] is truthy.")

if (1,):
    print("Non-empty tuple (1,) is truthy.")

if {"a": 1}:
    print("Non-empty dictionary {\"a\": 1} is truthy.")

if {1, 2}:
    print("Non-empty set {1, 2} is truthy.")

if range(1):
    print("Non-empty range range(1) is truthy.")

print("\n")

# --- 3. Truthy and Falsy in Conditional Statements (if/elif/else) --- #
"""
Truthy and falsy values are most commonly used in `if`, `elif`, and `else` statements.
Instead of explicitly comparing a value to `True` or `False`, you can directly use the value.
"""

print("--- Conditional Statements Examples ---")

# Example 1: Checking if a list is empty
my_list = [1, 2, 3]
if my_list:
    print(f"The list {my_list} is not empty (truthy).")
else:
    print(f"The list {my_list} is empty (falsy).")

my_empty_list = []
if my_empty_list:
    print(f"The list {my_empty_list} is not empty (truthy).")
else:
    print(f"The list {my_empty_list} is empty (falsy).")

# Example 2: Checking if a string has content
user_input = "Python"
if user_input:
    print(f"User input \"{user_input}\" is provided (truthy).")
else:
    print("User input is empty (falsy).")

empty_input = ""
if empty_input:
    print(f"User input \"{empty_input}\" is provided (truthy).")
else:
    print("User input is empty (falsy).")

# Example 3: Checking for a non-zero number
count = 5
if count:
    print(f"Count is {count} (truthy).")
else:
    print(f"Count is {count} (falsy).")

zero_count = 0
if zero_count:
    print(f"Count is {zero_count} (truthy).")
else:
    print(f"Count is {zero_count} (falsy).")

# Example 4: Using `None`
config_value = None
if config_value:
    print("Config value is set (truthy).")
else:
    print("Config value is not set (falsy).")

config_value_set = "some_value"
if config_value_set:
    print(f"Config value is \"{config_value_set}\" (truthy).")
else:
    print("Config value is not set (falsy).")

print("\n")

# --- 4. Truthy and Falsy in Loops (while) --- #
"""
Truthy and falsy values can also control `while` loops.
The loop continues as long as the condition evaluates to a truthy value.
"""

print("--- Loop Examples (while) ---")

# Example 1: Looping until a list is empty
queue = ["task1", "task2", "task3"]
print(f"Initial queue: {queue}")
while queue:
    task = queue.pop(0) # Remove first item
    print(f"Processing task: {task}. Remaining queue: {queue}")
print("Queue is empty, loop finished.")

print("\n")

# Example 2: Looping with a counter (non-zero is truthy)
counter = 3
print(f"Initial counter: {counter}")
while counter:
    print(f"Counting down: {counter}")
    counter -= 1
print("Counter reached 0, loop finished.")

print("\n")

# Example 3: Reading input until a non-empty string is provided
# This example is commented out to avoid blocking execution, but demonstrates the concept.
user_name = ""
while not user_name:
    user_name = input("Please enter your name: ")
    if not user_name:
        print("Name cannot be empty. Please try again.")
print(f"Hello, {user_name}!")

# Example 4: Using a flag variable
is_running = True
iteration = 0
while is_running:
    print(f"Application is running, iteration {iteration}")
    iteration += 1
    if iteration == 3:
        is_running = False # Set to falsy to stop the loop
print("Application stopped.")

print("\n")

# --- 5. Short-circuiting with `and` and `or` --- #
"""
Truthy and falsy values are fundamental to how `and` and `or` operators work in Python.
These operators use "short-circuit evaluation":

- `A and B`: If `A` is falsy, `A` is returned immediately, and `B` is not evaluated.
             Otherwise, `B` is evaluated and its value is returned.
- `A or B`: If `A` is truthy, `A` is returned immediately, and `B` is not evaluated.
            Otherwise, `B` is evaluated and its value is returned.
"""

print("--- Short-circuiting Examples ---")

# Example 1: `and` operator
result_and_1 = [] and "hello" # [] is falsy, so it's returned
print(f"[] and \"hello\" -> {result_and_1} (falsy)")

result_and_2 = "hello" and [] # "hello" is truthy, so [] is evaluated and returned
print(f"\"hello\" and [] -> {result_and_2} (falsy)")

result_and_3 = "hello" and "world" # "hello" is truthy, so "world" is evaluated and returned
print(f"\"hello\" and \"world\" -> {result_and_3} (truthy)")

result_and_4 = 0 and 10 # 0 is falsy, so it's returned
print(f"0 and 10 -> {result_and_4} (falsy)")

print("\n")

# Example 2: `or` operator
result_or_1 = [] or "hello" # [] is falsy, so "hello" is evaluated and returned
print(f"[] or \"hello\" -> {result_or_1} (truthy)")

result_or_2 = "hello" or [] # "hello" is truthy, so it's returned
print(f"\"hello\" or [] -> {result_or_2} (truthy)")

result_or_3 = 0 or False # 0 is falsy, False is falsy, so False is returned
print(f"0 or False -> {result_or_3} (falsy)")

result_or_4 = 10 or "world" # 10 is truthy, so it's returned
print(f"10 or \"world\" -> {result_or_4} (truthy)")

print("\n")

# --- 6. Custom Objects and Truthiness --- #
"""
For custom objects, Python determines truthiness based on the presence of `__bool__` or `__len__` methods.
- If `__bool__` is defined, it's called and its boolean result is used.
- If `__bool__` is not defined but `__len__` is, it's called and the object is truthy if `__len__` returns a non-zero integer.
- If neither is defined, all instances of the class are considered truthy by default.
"""

print("--- Custom Object Truthiness Examples ---")

class MyContainer:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    # __bool__ takes precedence over __len__ if both are defined
    # def __bool__(self):
    #     return len(self.items) > 1 # Custom logic

container_with_items = MyContainer([1, 2])
container_empty = MyContainer([])

if container_with_items:
    print(f"MyContainer with items {container_with_items.items} is truthy (due to __len__).")

if not container_empty:
    print(f"MyContainer with no items {container_empty.items} is falsy (due to __len__).")

class AlwaysTruthy:
    # No __bool__ or __len__ defined
    pass

always_truthy_obj = AlwaysTruthy()
if always_truthy_obj:
    print("An instance of AlwaysTruthy is always truthy by default.")

print("\n")

"""
Conclusion:
Mastering truthy and falsy values allows for more elegant, readable, and efficient Python code.
It's a core concept that simplifies conditional logic and loop control.
"""
