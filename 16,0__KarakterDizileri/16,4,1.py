import locale
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")


print(sorted("ağaçlar", key=locale.strxfrm))

