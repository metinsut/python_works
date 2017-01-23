dosya=open("çalışma1.txt","w")
print(*[metot for metot in dir(dosya) if not metot.startswith("_")],sep="\n")


print(dosya.close())