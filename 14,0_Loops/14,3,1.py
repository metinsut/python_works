for a in range(5,10):
    print(a)

while True:
    parola=input("Parolayı belirle: ")
    if not parola:
        print("Parola boş bırakılamaz ! ")
    elif len(parola) in range (3,8):
        print("Yeni parolanız", parola)
        break
    else:
        print("Parola 8 karakterden uzun yada 3 karakterden kısa olmamalı.")