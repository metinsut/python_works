çocuklar=["didem","metin","pınar","fırat"]
ebeveyn=["refik","fatma"]
aile=çocuklar+ebeveyn
print(aile)


sayılar = 0

for i in range(1,11):
    print(i,".","notunuzu girin")
    sayılar += int(input("not: "))

print(sayılar/10)