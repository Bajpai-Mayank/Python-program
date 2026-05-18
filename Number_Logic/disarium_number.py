def is_disarium_number(x):
    org=x
    total=0
    i=len(str(x))
    while(org>0):
        total+=(org%10)**i
        org//=10
        i-=1
    return total==x
try:
    x=int(input("Enter the number : "))
    print("Disarium Number") if is_disarium_number(x) else print("Not Disarium Number")
except ValueError:
    print("Invalid input! Please enter a number.")