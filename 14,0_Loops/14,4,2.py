
d1=open("isimler1.txt")
d1_satırlar=d1.readlines()

d2=open("isimler2.txt")
d2_satırlar=d2.readlines()

print(d2_satırlar, end="")

for i in d2_satırlar:
    if not i in d1_satırlar:
        print()
d1.close()
d2.close()