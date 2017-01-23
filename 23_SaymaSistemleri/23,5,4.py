print("{:b}".format(12))
print("{:x}".format(12))
print("{:o}".format(12))




a=int(input("Lütfen bir sayı giriniz ve o sayıya kadar diğer sayı sistemlerindeki karşılığını görün."))
sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]

print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))

for i in range(a):
    print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))

