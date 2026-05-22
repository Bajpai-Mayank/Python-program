import re
n=int(input("Enter the number: "))
s=f"{n*1}{n*2}{n*3}"
k=re.findall("[1-9]",s,re.DOTALL)
print("Fasinating number") if(len(set(k))==9) else print("Not Fasinating number")
