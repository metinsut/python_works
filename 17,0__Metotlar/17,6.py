a="Metin"
print(a.endswith("n"))

str1='"xxx"'
print("hi" if str1.startswith('"') and str1.endswith('"') else "fails")

d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"

for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    #if i.endswith(".mp3"):
     #   print(i)
    if i[-4:]==".mp3":
        print(i)