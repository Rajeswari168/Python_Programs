numbers = [10, -5, 8, -2, 15, -9, 20, 3, -12, 7]

try:
    index = int(input("Enter index (0-9): "))

    if numbers[index] > 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Enter a valid integer index.")