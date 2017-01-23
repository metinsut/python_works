print("Sitemize hoş geldiniz.")

kulad=input("Kullanıcı adınızı: ")
parola=input("Parolanız        : ")

toplam_uzunluk=len(kulad)+len(parola)

mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"

print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk>40:
    print("Kullanıcı adınız ile parolanız ",
          "toplam uzunluğu 40 karakteri geçmemeli!")
else:
    print("Sisteme hoşgeldiniz!")

input()