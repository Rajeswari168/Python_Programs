n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
t=tuple(l)
search=int(input("Enter element to search :"))
if search in t:
    print("Element exists")
else:
    print("Element does not exist")
