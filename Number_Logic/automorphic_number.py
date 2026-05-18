n= int(input("Enter the number : "))
size=len(str(n))
print("Automorphic Number") if(n==(n**2)%(10**size)) else print("Not Automorphic Number")
