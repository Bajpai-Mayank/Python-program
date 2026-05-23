def word_len(e):
    return len(e)
s=input("Text : ")
word=s.split()
max_order=s.split()
max_order.sort(reverse=True,key=word_len)
max_size=len(max_order[0])
print("*"*(max_size+4))
for i in word:
    x=max_size-len(i)
    print(f"* {i:<{x}} *")
print("*"*(max_size+4))