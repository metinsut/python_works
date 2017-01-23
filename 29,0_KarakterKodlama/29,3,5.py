import locale
print(locale.getpreferredencoding())

f=open("soru.txt", "r",encoding="utf-8",errors="replace")
f.read(50)
