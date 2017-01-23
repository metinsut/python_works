kalkış       = input("Kalkış yeri: ")
varış        = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayısı = input("Bilet sayısı: ")

metin = "{} noktasından {} noktasına, 14:30 hareket saatli \n" \
        "sefer için {} adına {} adet bilet ayrılmıştır!"

print(metin.format(kalkış, varış, isim_soyisim, bilet_sayısı))


