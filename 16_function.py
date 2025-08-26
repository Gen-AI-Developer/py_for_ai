# def keyword is used to define a function.
# def name_of_the_function():
#       body of the function
#       
def greet():
    print("Hello, Programmers")

greet()

# Two things your code must satisfy Readability and Reusebility
greet()
greet()
greet()
greet()

# now making it dynamic so that everyone can use it
def greet(name:str):
    print(f"Hello, {name}")

greet('Safdar Ali Shah')
greet('Azhar Ali Shah')
greet('Sohail Ali Shah')
greet('Junaid Ali Shah')

def greeting (name:str,message:str | None = None ,default:str|None = None):
    if message:
        print(f'{message}, {name}')
        print("Welcome to CDCP")
    else:
        default = "Hello"
        print(f'{default}, {name}')

greeting('Saleem')