kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

çeviri_tablosu=str.maketrans(kaynak,hedef)
print(çeviri_tablosu)
metin="Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(çeviri_tablosu))

print(chr(246))

for i in 79, 99, 85, 67, 73, 105, 71, 111, 115, 117, 83, 103:
    i=str(i)
    print(i.ljust(7,"."),chr(int(i)))