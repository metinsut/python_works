harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'

# sözlük={}
# for i in harfler:
#     sözlük[i]=harfler.index(i)



sözlük={i:harfler.index(i) for i in harfler}


print(sözlük)


isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]

liste={i:len(i) for i in isimler}
print(liste)
