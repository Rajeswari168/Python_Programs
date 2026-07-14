d = {}
n = int(input("Enter number of items: "))
for i in range(n):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    d[key] = value
search_key = int(input("Enter key to search: "))
if search_key in d:
    print("Key exists")
else:
    print("Key does not exist")