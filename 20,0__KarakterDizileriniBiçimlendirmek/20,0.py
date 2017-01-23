isim=input("Lütfen isminizi giriniz: ")
if len(isim)<=5:
    print(isim)
else:
    print(isim[:5],"...",sep="")



