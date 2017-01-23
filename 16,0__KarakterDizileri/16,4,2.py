harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
print(sorted(harfler, key=çevrim.get))

print(çevrim)