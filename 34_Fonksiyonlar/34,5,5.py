def fonksiyon(**parametreler):
    print(parametreler)

fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")


def kayıt_oluştu(**bilgiler):
    print("-"*30)

    for anahtar,değer in bilgiler.items():
        print("{:<10}: {}".format(anahtar,değer))

    print("-"*30)


kayıt_oluştu(ad="metin",soyad="süt",şehir="istanbul",tel="0542",okul="KOU",yaş="29")



def karşılık(*args,**kwargs):
    for sözcük in args:
        if sözcük in kwargs:
            print("{} = {}".format(sözcük,kwargs[sözcük]))
        else:
            print("{} kelimesi sözlükte yok!".format(sözcük))


sözlük={"kitap"         :"book",
        "bilgisayar"    :"computer",
        "programlama"   :"programming"}

karşılık("kitap","bilgisayar","programlama","fonksiyon",**sözlük)



def bas(*args,start="",**kwargs):
    for öğe in args:
        print(start+öğe,**kwargs)
bas("öğe1","öğe2","öğe3", start="#.")


