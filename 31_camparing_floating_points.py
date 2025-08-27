
if (0.2 + 0.1 == 0.3):
    print("0.2 + 0.1 is equal to 0.3")
else:
    print("0.2 + 0.1 is not equal to 0.3")

from math import isclose
a : float = 0.999
b : float = 1.0
print(f"{a} is close to {b}: {isclose(a, b,abs_tol=0.002)}")
print(f"{a} is close to {b}: {isclose(a, b,rel_tol=0.01)}")