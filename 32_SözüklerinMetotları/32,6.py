hava_durumu = {"İstanbul": "yağmurlu",
               "Adana": "güneşli",
               "İzmir": "bulutlu"}


yedekhd=hava_durumu

print(hava_durumu)
print(yedekhd)



hava_durumu["mersin"]="sisli"

print(hava_durumu)
print(yedekhd)


deneme=hava_durumu.copy()
print(deneme)

deneme["kars"]="karlı"

print(hava_durumu)
print(yedekhd)
print(deneme)