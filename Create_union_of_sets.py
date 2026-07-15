n1=int(input("Enter number of elements in set 1: "))
s1=set()
for i in range(n1):
    x=int(input("Enter element: "))
    s1.add(x)
n2=int(input("Enter number of elements in set 2: "))
s2=set()
for i in range(n2):
    x=int(input("Enter element: "))
    s2.add(x)
print("Union of sets: ", s1.union(s2))