s=input("Enter the text: ")
char_list=list(s+" ")
fq=1
st=[]
for i in range(len(char_list)-1):
    if char_list[i] == char_list[i+1]:
        fq+=1
    else:
        st.append(f"{char_list[i]}{fq}")
        fq=1
print("".join(st))