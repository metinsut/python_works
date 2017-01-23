while True:
    s=input("Bir sayı giriniz: ")
    if s=="iptal":
        break
    if len(s)<=3:
        continue
    print("En fazla üç haneli bir sayı girebilirsiniz.")