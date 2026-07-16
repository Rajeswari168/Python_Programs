def sum_list(lst):
    return sum(lst)
n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
print("Sum:",sum_list(lst))