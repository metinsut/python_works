import os

# print(dir(os))

print(os.name)



if os.name != "posix":
    print("Kusura bakmayın! Bu programı yalnızca Windows'ta kullanabilirsiniz!")
else:
    print("Hoşgeldin Linux kullanıcısı")




print(os.getcwd())
os.makedirs("DENEME")