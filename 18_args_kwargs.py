def add(*args:int)-> int:
    print(args)
    return sum(args)
print(add(1,2,3,4,5,6))
#######################################
def add(*numbers:int)-> int:
    print(numbers)
    return sum(numbers)
print(add(1,2,3,4,5,6))
#######################################
def pin_position(**kwargs:int)-> int:
    print(kwargs)
pin_position(x=10,y=102)
###################################
def numbers(*args,**kwargs)-> None:
    print(args)
    print(kwargs)
numbers(1,23,4,5,6,x=12,y=34,z=453)