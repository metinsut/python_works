sayı_sistemleri = ["onlu", "sekizli", "on altılı"]

print(("{:^8} "*len(sayı_sistemleri)).format(*sayı_sistemleri))

for i in range(17):
    print("{0:^8} {0:^8o} {0:^8x}".format(i))