#kelime = input("Herhangi bir kelime: ")

#for harf in kelime:
#    print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf,kelime,kelime.count(harf)))


kelime = input("Herhangi bir kelime: ")
sayaç = ""

for harf in kelime:
    if harf not in sayaç:
        sayaç += harf
        print(sayaç)
for harf in sayaç:
    print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf,kelime,kelime.count(harf)))

for harf in sayaç:
    print(harf, kelime, kelime.count(harf))
