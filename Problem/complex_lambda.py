data = [("Alice", 25, 90), ("Bob", 20, 80), ("Charlie", 22, 90), ("Dave", 25, 85)]
sorted_data = sorted(data, key=lambda x: (-x[2], x[1]))
even_data = list(filter(lambda x:x[2]%2==0,data))
double_data = list(map(lambda x:x[2]**2,data))
print(sorted_data)
print(even_data)
print(double_data)