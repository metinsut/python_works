# soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın:")
#
# if soru=="istanbul":
#     print("Gök gürültülü ve sağanak yağışlı.")
# elif soru=="ankara":
#     print("Açık ve güneşli")
# elif soru=="izmir":
#     print("Bulutlu")
# else:
#     print("Bu şehre ait bilgi bulunmamaktadır.")



soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın:")

cevap={"istanbul": "gök gürültülü ve sağanak yağışlı",
         "ankara": "açık ve güneşli", "izmir": "bulutlu"}
print(cevap.get(soru, "Bu şehre ilişkin bilgi yok"))

