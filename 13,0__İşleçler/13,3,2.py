kulad="metin"
parol=1234

kullanıcı_adı=str(input("Lütfen 5 Harfli kullanıcı adınızı girin:"))
parola=int(input("Lütfen 4 haneli parolanızı girin:"))

if kulad==kullanıcı_adı and parol==parola:
    print("Bilgileriniz doğru sisteme girebilirsiniz...")
else:
    print("Malesef girdiğiniz bilgiler yanlış.")