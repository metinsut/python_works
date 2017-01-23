# liste=[i for i in range(100)]:
liste=[]
for i in range(10):
    liste+=[i]
print(liste)

# for i in liste:
#     print(i)


sayıl=list(range(10))
print(sayıl)

metin=[i for i in range(10) if i%2==0]
print(metin)

fırat=[]
for i in  range(20):
    if i%2==0:
        fırat+=[i]
print(fırat)
print(type(fırat))