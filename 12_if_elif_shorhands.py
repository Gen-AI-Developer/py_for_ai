number : int = 10

if number > 0:
    result: str = "Above 0"
else:
    result: str = "below 0"
print(result)

number =-12
result : str = "Above 0" if number>0 else '0 and Below'
print(result)

condition : bool = True
var: str = 'True' if condition else 'False'
print(var)