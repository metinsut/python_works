hakkında=open("isimler1.txt")
harf=input("Sorgulamak istediğiniz harf: ")
sayı=0
for karakter_dizisi in hakkında:
    for karakter in karakter_dizisi:
        if harf == karakter:
            sayı+=1
print(sayı)

hakkında.close()