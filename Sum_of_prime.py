import sys

sum = 0

for i in range(1, len(sys.argv)):
    n = int(sys.argv[i])

    prime = True

    if n < 2:
        prime = False
    else:
        for j in range(2, n):
            if n % j == 0:
                prime = False
                break

    if prime:
        sum += n

print("Sum of Prime Numbers =", sum)