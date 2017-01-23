# def kare_bul():
#     sayı=12
#     çıktı="{} sayısının karesi {} sayısıdır."
#     print(çıktı.format(sayı,sayı**2))
#
#
# kare_bul()




def kare_bul(sayı):
    çıktı = "{} sayısının karesi {}, karekökü ise {} sayısıdır."
    print(çıktı.format(sayı, sayı ** 2,(sayı**0.5)))

kare_bul(16)
kare_bul(9)


def uzunluk(öğe):
    c=0
    for s in öğe:
        c+=1
    print(c)



uzunluk("Metin Süt")