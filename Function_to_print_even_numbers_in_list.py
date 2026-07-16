def even_numbers(lst):
    for i in lst:
        if i%2==0:
            print(i, end=" ")
n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
even_numbers(lst)