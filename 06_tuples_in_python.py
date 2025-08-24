# the major difference between lists and tuples 
# is that tuples are immutable, 
# which means once created can't be change
# which makes it more memory efficient..  
items: tuple = 1,2,3,True,False
print(type(items))
print(items)


coordinates = ()
print(type(coordinates))

coordinates: tuple[float,float] = 34.444,54.3333
print(coordinates)