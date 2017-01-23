sözlük={"metin":"29"}

print(sözlük)
print(sözlük["metin"])


harf={"a": 0,
      "b": 1,
      "c": 2,
      "d": 3}


print(sözlük.keys())
print(harf.keys())


liste=list(harf.keys())
print(liste)

liste1=tuple(harf.keys())
print(liste1)

liste2="-".join(harf.keys())
print(liste2)


