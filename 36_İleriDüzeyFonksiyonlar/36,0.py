fonk=lambda p1,p2:p1+p2

print(fonk(5,3))



harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}

isimler = ["ahmet", "ışık", "ismail", "çiğdem","can", "şule", "iskender"]

print(sorted(isimler, key=lambda x: çevrim.get(x[0])))


lambda x:x+10

