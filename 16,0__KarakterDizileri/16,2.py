site="www.istihza.com"
print(site[1:10])

k="istanbul"
print(k[0:3])


s1="www.google.com"
s2="www.istihza.com"
s3="www.yahoo.com"
s4="www.gnu.org"

for isim in s1,s2,s3,s4:
    print("Site: ", isim[4:-4])

ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca  kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"

for ata in ata1,ata2,ata3,ata4,ata5:
    print(ata[0:-1]+".")