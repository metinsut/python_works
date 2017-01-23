print("Çekoslavakyalılardanmısınız".count("a"))
print("adana".count("a",2))



parola=input("Parolanızı girin: ")
kontrol=True
for i in parola:
    if parola.count(i)>1:
        kontrol=False
if kontrol:
    print("Parolanız onaylandı!")
else:
    print("Parolanızda aynı harfi bir kez kullanabilirsiniz!")



m=input("gir")
for i in m:
    if m.count(i)>1:
        print("Aynı rakamı girme")
    else:
        print("tamamdır")