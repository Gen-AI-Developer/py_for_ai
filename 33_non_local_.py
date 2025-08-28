def outer_func()-> None:
    name: str = ""
    address: str = ""
    def inner_func():
        nonlocal name, address
        name = "safdar"
        address = "peshawar"
        print("Inner Function Values..", name, address)
    inner_func()
    print("Outer Function = Name", name)
    print("Outer Function = address", address)
    
    
       

def main():
    print("Outer Function Values..")
    outer_func()

if __name__=="__main__":
    main()
    