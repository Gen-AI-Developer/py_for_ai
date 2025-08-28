number : int = 0

def func()-> None:
    print("func() Called")
    global number
    number = number + 10
    print("func() executed")

def main():
    print("Old Value of Number: ", number)
    print("calling func()")
    func()
    print("New value of number : ", number)

if __name__=="__main__":
    main()
    