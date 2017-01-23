# x=0
# def fonk():
#     x=1
#     return x
#
# print('fonksiyon içindeki x: ', fonk())
# print('fonksiyon dışındaki x: ', x)


# x = 0
#
# def fonk():
#     x = 10
#     print(x)
#
# fonk()
# print(x)


x = set()

def fonk():
    x.add(10)
    return x

print(fonk())


isim = 'Fırat'

def fonk():
    global isim
    isim += ' Özgül'
    return isim

print(fonk())


