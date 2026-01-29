print("<Sorting Program>")

list_num = []
for i in range(3):
    number = int(input(f"Enter Value {i+1}: "))
    list_num.append(number)
print("[Before Sorting]")
for i in range(3):
    print(f"{list_num[i]}", end="")
print()

list_num.sort()

print("[After Sorting]")
for i in range(3):
    print(f"{list_num[i]}", end="")