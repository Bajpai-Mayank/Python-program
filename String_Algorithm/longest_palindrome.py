s=input("Text: ")
l,r=0,len(s)
max_str=""
while(l<=r):
    if(l==r):
        l+=1
        r=len(s)
        continue
    temp=s[l:r]
    r-=1
    rev_temp="".join(reversed(temp))
    if  temp == rev_temp and len(max_str)<len(rev_temp) and l!=r:
        max_str=temp
        break
print(max_str)

