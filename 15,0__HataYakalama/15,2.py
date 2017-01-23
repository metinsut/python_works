ilk_sayı=input("İlk sayı: ")
ikinci_sayı=input("İkinci sayı: ")

try:
    sayı1=int(ilk_sayı)
    sayı2=int(ikinci_sayı)
    print(sayı1,"/",sayı2,"=",sayı1/sayı2)
except ValueError:
    print("Lütfen sadece sayı giriniz!")
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")
