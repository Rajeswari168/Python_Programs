n = int(input("Enter number of elements: "))
d = {}
for i in range(n):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    d[key] = value
total = sum(d.values())
print("Sum =", total)