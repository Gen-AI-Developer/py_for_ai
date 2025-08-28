numbers: list[int] = [1, 2, 3, 4, 5]

doubled: list[int] = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)

doubled_lc: list[int] = [n * 2 for n in numbers]
print(doubled_lc)

names_with_A : list[str] = ["Alice", "Bob", "Charlie", "Alan","Ali","Alex"]

for name in names_with_A:
    if name.startswith("A"):
        names_with_A.append(name)
print(names_with_A)


names_with_B: list[str] = ['Brown','bobby','Alex','Charlie',"Jgango"]

names_with_B_lc = [name
                   for name in names_with_B
                   if name.lower().startswith("b")]

print(names_with_B_lc)