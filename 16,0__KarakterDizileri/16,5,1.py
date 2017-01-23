sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"

sesliler = ""
sessizler = ""

kelime = "istanbul"

for i in kelime:
    if i in sesli_harfler:
        sesliler += i
    else:
        sessizler += i

print("sesli harfler: ", sesliler)
print("sessiz harfler: ", sessizler)

