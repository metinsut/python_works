print("Metin, Fırat, Pınar ve Didem ailenin çocuklarıdır")
print("Metin\nFırat\nPınar\nDidem")
print("birinci satır","ikinci satır","üçüncü satır", sep="\n")
print("Bugün günlerden salı.", end=".")
print(55555555)

print("bir","iki","üç","dört","on dört",sep=" mumdur ", end=" mumdur\n")
print(5555)

print("metin",end="")
print(11)

print("Ben Metin, Metin Süt!")

dosya=open("deneme.txt","w")
print("Ben Metin, Metin Süt!", file=dosya)
dosya.close()

f=open("Kişisel Bilgiler.txt","w")
print("Metin", file=f)
print("Beykoz",file=f)
print("Python Öğreniyor",file=f)
f.close()


input()

