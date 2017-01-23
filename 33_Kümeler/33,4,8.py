k1=set([1, 2, 3, 4])
k2=set([1, 3, 5, 7])
print(k1.intersection(k2))


tr = "şçöğüıŞÇÖĞÜİ"
parola = input("Sisteme giriş için bir parola belirleyin: ")
if set(tr)&set(parola):
    print("Türkçe karakter yok!")
else:
    print("Parolanız kabul edildi!")


