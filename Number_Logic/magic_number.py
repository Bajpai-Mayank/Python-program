def isMagicNumber(x):
    sum=0
    while(x>0):
        sum+=(x%10)**2
        x//=10
    return sum
x=int(input("Enter the value : "))
num = set()
while x not in num and x !=1:
    num.add(x)
    x=isMagicNumber(x)

if x == 1:
    print("Magic Number")
else:
    print("Not Magic Number")
