ing_sözlük = {"dil": "language",
              "bilgisayar": "computer",
              "masa": "table"}


sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")


print(ing_sözlük.get(sorgu, "Bu kelime lsitede yok"))

