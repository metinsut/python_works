a="python"
print(a.capitalize())

kardiz = "istanbul büyükşehir belediyesi"

if kardiz.startswith("i"):
    kardiz = "İ" + kardiz[1:]

kardiz = kardiz.capitalize()

print(kardiz)

print("istanbul".capitalize())


kardiz = "istanbul"
print(kardiz[1:len(kardiz)])

