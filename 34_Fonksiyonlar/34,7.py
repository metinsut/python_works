import random
def sayı_üret(başlangıç=0,bitiş=500,adet=6):
    sayılar=set()

    while len(sayılar)<adet:
        sayılar.add(random.randrange(başlangıç,bitiş))
    return sayılar


for i in range(5):
    print(*sayı_üret(1,49,6),sep="-")


