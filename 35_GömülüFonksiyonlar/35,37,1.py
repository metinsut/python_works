notlar = {'Ahmet'   : 60,
          'Sinan'   : 50,
          'Mehmet'  : 45,
          'Ceren'   : 87,
          'Selen'   : 99,
          'Cem'     : 98,
          'Can'     : 51,
          'Kezban'  : 100,
          'Hakan'   : 66,
          'Mahmut'  : 80}



def not_durumu(n):
    if n in range(0,50):return "F"
    if n in range(50,70):return "D"
    if n in range(70,80):return "C"
    if n in range(80,90):return "B"
    if n in range(90,100):return "A"



print(not_durumu(54))



def süz(n):
    return n>=70

print(*filter(süz,notlar.values()))

