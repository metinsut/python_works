"""
ilk_metin="13597"
ikinci_m="1245689"

for s in ilk_metin:
    if not s in ikinci_m:
        print(s, end="")
"""
ad1="metinsüt"
ad2="fıratsüt"
fark=""
for s in ad2:
     if not s in ad1:
         if not s in fark:
             fark += s
             print(id(fark),fark)
print(id(fark),fark)

for s in ad2:
    if not s in ad1 and not s in fark:
        fark+=s
print(fark)
