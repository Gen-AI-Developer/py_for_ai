# keyword and Positional Arguments

def funct(var_a:str,/,var_b:str):
    print(var_a)
    print(var_b)
    
funct('safdar',var_b='ali')

def func(var_a:str,*,var_b:str):
    print(var_a)
    print(var_b)
    
func('ali',var_b='safdar')

def func(var_a:str,/,var_b:str,*,var_c:str):
    print(var_a)
    print(var_b)
    print(var_c)
    
func('ali',var_b='safdar',var_c="shah")