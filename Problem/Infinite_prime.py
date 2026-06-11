import itertools
def prime_generator():
    k,ct=1,0
    while True:
        for i  in itertools.count(start=1):
           if k%i==0:
                ct+=1
           if i==k:
               break
        if ct == 2:
            yield k
        ct=0
        k+=1
prime=prime_generator()
for _ in range(5):
    print(next(prime))