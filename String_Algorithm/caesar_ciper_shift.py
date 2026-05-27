n= int(input("Shift : "))
s= input("Text: ")
if(n>=26):
    n=n%26
new_str=[]
words=s.split()
for i in words:
    for j in i:
        if ord(j) == 80 :
            shift=ord('A')+n
        elif ord(j) == 122:
            shift=ord('a')+n
        else:
            shift=ord(j)+n
        new_str.append(chr(shift))
    new_str.append(" ")
print("".join(new_str))
