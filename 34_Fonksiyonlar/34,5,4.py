def fonksiyon(*parametreler):
    print(parametreler)



fonksiyon(1,2,3,4,5)



def çarp(*sayılar):
    sonuç = 1
    for i in sayılar:
        sonuç *= i
    print(sonuç)



çarp(5,2,3)

def deneme(*args):
    print(args)

deneme(123)