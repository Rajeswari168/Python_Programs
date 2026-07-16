def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return true
n=int(input("Enter a number:"))
if is_prime(n):
    print(n,"is a prime number")
else:
    print(n, "is not a prime number")