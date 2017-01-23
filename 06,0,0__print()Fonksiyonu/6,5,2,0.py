import os
import sys



print(os.getcwd())



m=open("ciddi misin.txt","w")

sys.stdout = m
print(sys.stdout)

print("Metin Süt",file=m)
print("İstanbul","Beykoz",sep="/",file=m)
print("Python öğreniyor",file=m)

print("Bunu yaz lan dosyanın içine")



m.close()




input()


