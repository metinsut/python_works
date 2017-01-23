kardiz = input("Metin girin: ")
aranacak = input("Aradığınız harf: ")

for i in range(len(kardiz)):
    print("i'nin değeri: ", i)
    if i == kardiz.index(aranacak, i):
        print("%s. sırada 1 adet %s harfi bulunuyor" %(i, aranacak))
    else:
        print("%s. sırada %s harfi bulunmuyor" %(i, aranacak))