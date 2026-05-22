n=int(input("Enter the number: "))
state=False
for i in range(n):
    if(n==(i*(i+1))):
        state=True
        break
if(state):
    print("Pronic Number")
else:
    print("Not Pronic Number")
