sayılar="123456789"
for sayı in sayılar:
    print(int(sayı)*2)

for s in "Metin":
    print(s)

sayılar="123456789"
for i in sayılar:
    if int(i)>3:
        print(i)
    else:
        print("Olmadı yar")

tr_harfler="şçöğüİı"
parola=input("Parolanız: ")
for karakter in parola:
    if karakter in tr_harfler:
        print("parolada Türkçe karakter kullanılmaz.")