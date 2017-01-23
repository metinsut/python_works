for k in range(-1000, 1000):
     for v in range(-1000, 1000):
         if k is v:
             print(k)

a=10001
print(id(a))
print(id(10001))
print(a is 10001)


