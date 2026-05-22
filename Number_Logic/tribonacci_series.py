def tribo(n):
   a,b,c=0,1,2
   print(f"{a} , {b} , {c}",end=" ")
   for i in range(n):
    a,b,c=b,c,a+b+c
    print(f" , {c}",end="") 
tribo(10)
