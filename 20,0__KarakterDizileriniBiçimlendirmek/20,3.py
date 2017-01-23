print(*enumerate(dir("")))
for i,b in enumerate(dir(""),1):
    print(i,b)

sayaç = 0

for i in dir(""):
    if "_" not in i[0]:
        sayaç += 1
        print(sayaç, i)