liste=["elma","armut","çilek"]
liste.insert(1,"erik")
print(liste)
liste.insert(len(liste),"karpuz")
print(liste)

f = open("deneme.txt", "r")
içerik = f.readlines()
içerik.insert(1, "Ferhat Yaz\n")

g = open("deneme.txt", "w")
g.writelines(içerik)



f.close()
g.close()




