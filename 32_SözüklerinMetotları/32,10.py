sepet={"meyveler": ("elma", "armut"),
       "sebzeler": ("pırasa", "fasulye"),
       "içecekler": ("su", "kola", "ayran")}


print(sepet.setdefault("meyveler",("erik","çilek")))

print(sepet)

print(sepet.setdefault("yemekler",("patlıcan","pilav")))
print(sepet)