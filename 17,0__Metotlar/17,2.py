ad="İstanbul Büyükşehir Belediyesi"
print(ad.split())

for i in ad.split():
    print(i)

kısalt=input("Kısaltılacak kurumu girin: ")
for i in kısalt.split():
    print(i[0],end="")