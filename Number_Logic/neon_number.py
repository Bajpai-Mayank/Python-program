x=int(input("Enter the number : "))
orgx=x**2
total=0
while orgx>0:
    total+=orgx%10
    orgx//=10
print("Neon Number") if total==x else print("Not Neon Number")