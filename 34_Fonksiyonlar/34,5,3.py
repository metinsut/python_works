def kur(kurulum_dizini="/usr/bin/"):
    print("Program {} dizinine kuruldu!".format(kurulum_dizini))


kur("c:\\Users\\metin")




def kur(kurulum_dizini=''):
    if not kurulum_dizini:
        print("Lütfen programı hangi dizine kurmak istediğinizi belirtin!")
    else:
        print("Program {} dizinine kuruldu!".format(kurulum_dizini))


kur("a")




