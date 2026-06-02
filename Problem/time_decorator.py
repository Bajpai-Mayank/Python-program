import time as t
import random as rand
intial_time= t.perf_counter()
for i in range(6):
    print("Dice : ",rand.randint(1,6))
final_time=t.perf_counter()
print("Excution Duaration to perform Given task : ",final_time-intial_time)
