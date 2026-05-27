import re
s=input("Text: ")
if(len(set(re.findall("[a-z]",s,re.IGNORECASE)))==26):
    print("Pangram")
else:
    print("Not Pangram")