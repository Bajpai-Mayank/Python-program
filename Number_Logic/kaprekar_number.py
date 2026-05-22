n=input("Enter the number : ")
l=len(n)
n=int(n)
orgn=n*n
sum=0
while(orgn>0 and len(str(n*n))%2==0):
    sum+=orgn%(10**l)
    orgn//=(10**l)
if(sum==n):
    print("Kaprekar Number")
else:
    print("Not-Kaprekar Number")
