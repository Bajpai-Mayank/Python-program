import re
s=input("Text : ").lower()
#1.Easiest Approach with regex : findall or search
new_str=re.findall("[^aeiou]",s)
print("".join(new_str).upper())
#2. Without using regex
new_str2=s
vowel=['a','e','i','o','u']
for i in vowel:
    new_str2=new_str2.replace(i,"")
print(new_str2.upper())