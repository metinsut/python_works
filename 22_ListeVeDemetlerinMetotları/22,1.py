# print(*dir([]),sep="\n")
# print(*[i for i in dir([]) if not "_" in i])

liste=["elma","armut","çilek"]
print(liste)
liste.append("erik")
print(liste)
liste+=["karpuz"]
print(liste)


# işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
# platformlar = ["IPhone", "Android", "S60"]
# hepsi = işletim_sistemleri + platformlar
# print(hepsi)



işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]
isimler=["metin","fırat"]
hepsi=[]
for i in işletim_sistemleri+platformlar+isimler:
    hepsi.append(i)
print(hepsi)




# sonuç=1
# while True:
#     sayı=input("sayı (hesaplamak için q): ")
#     if sayı=="q":
#         break
#     sonuç*=int(sayı)
# print(sonuç)


# print("Çarpma işlemi programına hoşgeldiniz.")
# print("İki veya daha fazla sayı giriniz sonra işlemi yapmak için q tuşuna basın:")
#
# kontrol=[]
# sonuç=1
# while True:
#     sayı=input("Bir sayı giriniz: ")
#     if sayı=="q":
#         break
#     kontrol.append(sayı)
#     sonuç*=int(sayı)
#     print(*kontrol,sep="*")
# if len(kontrol)<2:
#     print("Lütfen istenen şartları sağlayınız...")
# else:
#     print(sonuç)