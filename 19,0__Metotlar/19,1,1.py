çeviri_tablosu = {"Ö": "O",
                  "ç": "c",
                  "Ü": "U",
                  "Ç": "C",
                  "İ": "I",
                  "ı": "i",
                  "Ğ": "G",
                  "ö": "o",
                  "ş": "s",
                  "ü": "u",
                  "Ş": "S",
                  "ğ": "g"}

print(çeviri_tablosu["ş"])


print("deneme".translate(str.maketrans("metin","fırat")))
import string

metin = u"Pşhotı wdubdjhdı btj oti ösu ysl. ÖFMRVhdı mtıuf jdıysıs btj fikri ösu ysl wsös wxugıgştuç Id jfyfu qfnlf xeudımdı t jfyfu djmsesı \
tlyaeaıa fılrştumaı. kghosi ösuidşççç"
kaynak= u"qQwWeErRtTyYuUıIoOpPğĞüÜaAsSdDfFgGhHjJkKlLşŞiİ,,zZxXcCvVbBnNmMöÖçÇ.."
hedef = u"fFgGğĞıIoOdDrRnNhHpPqQwWuUiİeEaAüÜtTkKmMlLyYşŞxXjJöÖvVcCçÇzZsSbB..,,"

sozluk = {}

for k, v in zip(kaynak, hedef):
    sozluk[ord(k)] = v

soncevir = metin.translate(sozluk)
print(soncevir)