"""while True:
    soru=input("Nasılsınız beyfendi.")
    if soru=="q":
        break
"""


"""
tekrar=1
while tekrar<=3:
    tekrar+=1
    input("Nasılsınız iyimisiniz.")
"""


tekrar = 1
while tekrar <= 3:
    print("tekrar: ", tekrar)
    tekrar += 1
    input("Nasılsınız, iyi misiniz?")
    print("bool değeri: ", bool(tekrar <= 3))