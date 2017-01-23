print("metin".replace("i","İ").upper())

şehir = input("Hava durumunu öğrenmek için bir şehir adı girin: ")
şehir=şehir.upper()
if şehir == "ADANA":
    print("parçalı bulutlu")

elif şehir == "ERZURUM":
    print("karla karışık yağmurlu")

elif şehir == "ANTAKYA":
    print("açık ve güneşli")

else:
    print("Girdiğiniz şehir veritabanında yok!")
