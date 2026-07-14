n = int(input("Enter number of elements: "))
l = []
for i in range(n):
    x = int(input("Enter element: "))
    l.append(x)
t = tuple(l)
print("4th element from first:", t[3])
print("4th element from last:", t[-4])