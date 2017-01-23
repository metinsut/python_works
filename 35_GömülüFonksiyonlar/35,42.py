askerler = {'ahmet'     : 'onbaşı',
            'mehmet'    : 'teğmen',
            'ali'       : 'yüzbaşı',
            'cevat'     : 'albay',
            'berkay'    : 'üsteğmen',
            'mahmut'    : 'binbaşı'}



def en_yüksek_rütbe(rütbe):
    rütbeler = {'er'        : 0,
                'onbaşı'    : 1,
                'çavuş'     : 2,
                'asteğmen'  : 3,
                'teğmen'    : 4,
                'üsteğmen'  : 5,
                'yüzbaşı'   : 6,
                'binbaşı'   : 7,
                'yarbay'    : 8,
                'albay'     : 9}
    return rütbeler[rütbe]


print(max(askerler.values(), key=en_yüksek_rütbe))


for k,v in askerler.items():
    if askerler[k] in max(askerler.values(),key=en_yüksek_rütbe):
        print(v,k)

