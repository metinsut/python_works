a="metin"
print(a.islower())

veri=input("Adınız: ")
if not veri.islower():
    print("Lütfen isminizi sadece küçük harflerle yazın.")
else:
    print("Tamamdır",veri,"oldu.")

b="METIN"
print(b.isupper())