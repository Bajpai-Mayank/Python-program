n=input("Enter the number : ")
x=len(n)
n=int(n)
org_n=n
total=0
if(x%2!=0 and x!=0):
    print("Not Tech Number")
else:
    while(n>0):
        total+=n%100
        n//=100
    if(total**2 == org_n):
        print("Tech Number")
    else:
        print("Not Tech Number")