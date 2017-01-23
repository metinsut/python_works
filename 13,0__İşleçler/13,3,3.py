x=int(input("Notunuzu Girin: "))

if x>100 or x<0:
    print("Böyle bir not olamaz\nLütfen tekrar giriniz.")
elif x>=90 and x<=100:
    print("A aldınız.")
elif x>=80 and x<90:
    print("B aldınız.")
elif x>=70 and x<80:
    print("C Aldınız.")
elif x>=60 and x<70:
    print("D Aldınız.")
else:
    print("F aldınız.")