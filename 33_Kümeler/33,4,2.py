küme = set(["elma", "armut", "kebap"])

küme.add("çilek")
print(küme)


yeni=(1,2,3)
for i in yeni:
    küme.add(i)

print(küme)
print(type(küme))


küme.add(("asd"))
print(küme)


