while True:
    parola=input("Bir parola belirleyin: ")

    if not parola:
        print("Parola bölümü boş geçilmez!")
    elif len(parola)>8 or len(parola)<3:
        print("Parola 8 karakterden uzun 3 karakterden kısa olmamalı.")
    else:
        print("Yeni parolanız:", parola)
        break