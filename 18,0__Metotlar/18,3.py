print("Metin".swapcase())
print("FIRat".swapcase())


kar="izmir"
for a in kar:
    if a=='İ':
        kar=kar.replace("İ","i")
    elif a=="i":
        kar=kar.replace("i","İ")
    else:
        kar=kar.replace(a,a.swapcase())
print(kar)