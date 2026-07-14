dic1 = {}
dic2 = {}
dic3 = {}
n1 = int(input("Enter number of items in dic1: "))
for i in range(n1):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    dic1[key] = value
n2 = int(input("Enter number of items in dic2: "))
for i in range(n2):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    dic2[key] = value
n3 = int(input("Enter number of items in dic3: "))
for i in range(n3):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    dic3[key] = value
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print("Merged Dictionary:", result)