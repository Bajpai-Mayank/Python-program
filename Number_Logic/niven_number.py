try:
    x = int(input("Enter the number: "))
    
    total = 0
    for digit in str(x):
        total += int(digit)

    print("Niven Number") if x % total == 0 else print("Not Niven Number")

except ValueError:
    print("Invalid input! Please enter a number.")