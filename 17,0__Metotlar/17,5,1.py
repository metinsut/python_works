print("METIn".isupper())

veri = input("mesajınız: ")
böl = veri.split()

for i in böl:
    print(i)
    if i.isupper():
        print("Tamamı büyük harflerden oluşan kelimeler kullanmayın!")