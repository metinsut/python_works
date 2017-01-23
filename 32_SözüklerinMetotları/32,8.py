sepet = {"meyveler": ("elma", "armut"),
         "sebzeler": ("pırasa", "fasulye"),
         "içecekler": ("su", "kola", "ayran")}



sil=input("Silinecek yemek grubunu yazın")
print(sepet.pop(sil,"bu yemek grubu zaten yok"))