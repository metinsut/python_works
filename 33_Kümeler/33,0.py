boş_küme=set()

print(type(boş_küme))


# küme=set(["elma","armut","kebap"])

bilgi = {"işletim sistemi": "GNU",
         "sistem çekirdeği": "Linux",
         "dağıtım": "Ubuntu GNU/Linux"}

liste=[(anahtar,değer) for anahtar, değer in bilgi.items()]
küme=set(liste)
print(küme)