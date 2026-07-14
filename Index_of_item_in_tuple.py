n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
t=tuple(l)
item=int(input("Enter item to find index: "))
print("Index of item:", t.index(item))