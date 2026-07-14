n = int(input("Enter number of elements: "))
d = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Keys:")
for k in d:
    print(k)

print("Values:")
for v in d.values():
    print(v)

print("Keys and Values:")
for k, v in d.items():
    print(k, v)