tr_karakter = "şçğüöıİ"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass

print("Parola kabul edildi!")

input()

bölünen = int(input("bölünecek sayı: "))

if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

bölen = int(input("bölen sayı: "))
print(bölünen/bölen)