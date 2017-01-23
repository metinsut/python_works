print(30%4)

sayı =int(input("Bir sayı giriniz: "))

if sayı % 2 == 0:
    print("Girdiğiniz sayı bir çift sayıdır.")
else:
    print("Girdiğiniz sayı bir tek sayıdır.")

bölünen = int(input("Bir sayı giriniz: "))
bölen=int(input("Bir sayı daha giriniz"))

şablon="{} sayısı {} sayısına tam".format(bölünen,bölen)

if bölünen%bölen==0:
    print(şablon, "Bölünüyor!")
else:
    print(şablon, "bölünüyor!")
