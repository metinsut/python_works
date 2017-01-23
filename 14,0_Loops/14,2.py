
tr_harfler="şçöğüİı"
for harf in tr_harfler:
    print(harf)


tr_harfler="şçöğüİı"
print(*tr_harfler, sep="\n")


tr_harfler="şçöğüİı"
a=0

while a < len(tr_harfler):
    print(tr_harfler[a], sep="\n")
    a+=1