sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(n):
    for harf in kelime:
        if seslidir(harf):
            n += 1
    return n

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır(sayaç)))