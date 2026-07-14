d = {}
n = int(input("Enter number of key-value pairs: "))
for i in range(n):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    d[key] = value
new_key = int(input("Enter new key: "))
new_value = int(input("Enter new value: "))
d[new_key] = new_value
print("Updated Dictionary:", d)