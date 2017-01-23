parola=input("Parola: ")
print("Girdiğiniz parola (%s) kurallara uygun bir paroladır!" %parola)
print("%s ve %s iyi bir ikilidir!"%("Python","Django"))
print("%s adlı kişinin mekanı www.%s.com adresidir."%(parola,parola))
print("https://www.google.com")
parola=parola.replace("i","İ")
for sıra,karakter in enumerate(parola,1):
    print("%s. karakter: '%s'" %(sıra,karakter.upper()))