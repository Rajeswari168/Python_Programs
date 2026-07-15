n=int(input("Enter number of elements: "))
s=set()
for i in range(n):
    x=int(input("Enter elements:"))
    s.add(x)
print("Maximum:",max(s))
print("Minimum:",min(s))