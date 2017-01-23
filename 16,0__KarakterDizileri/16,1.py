object="fırat"
print(object)

data=input("Herhangi bir şey: ")
print(data,"\n")
for karakter in object:
    print(karakter)
print("")
for k in data:
    print(*k,sep="\n")