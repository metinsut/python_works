sayı =int(input("Bir sayı giriniz: "))
if sayı>10:
    print("Girdiğiniz sayı 10'dan büyüktür.")
if sayı<10:
    print("Girdiğiniz sayı 10'dan küçüktür.")
if sayı==10:
    print("Girdiğiniz sayı 10'a eşittir.")

print("""
Dünyanın en gelişmiş e.posta hizmetine
hoşgeldiniz. Yalnız hizmetimizden
yararlanmak için önce sisteme giriş
yapmalısınız.
""")

parola = input("Parola: ")

if parola == "1234":
    print("Sisteme Hoşgeldiniz!")
if parola != "12345678":
    print("Ne yazık ki yanlış parola girdiniz!")