k="istanbul işçiler şartnamesi ısınması"
for i in k.split():
    if i.startswith("i"):
        i="İ"+i[1:]

    i=i.title()
    print(i,end=" ")

print("\n")

m="on iki ada"
for i in m.split():
    if i.startswith("i"):
        i="İ"+i[1:]
    i=i.title()
    print(i[0])