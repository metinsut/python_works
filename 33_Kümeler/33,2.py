kardiz="Python Programlama Dili"
küme=set(kardiz)
print(küme)


liste = ["elma", "armut", "elma", "kebap", "şeker", "armut","çilek","ağaç", "şeker", "kebap", "şeker"]

for i in set(liste):
    print(i)

for i in set(liste):
    print("{} listede {} kez geçiyor!".format(i,liste.count(i)))


    