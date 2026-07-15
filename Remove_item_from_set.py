n=int(input("Enter number of elements: "))
s=set()
for i in range(n):
    x=int(input("Enter element:"))
    s.add(x)
item=int(input("Enter item to remove:"))
s.remove(item)
print(s)