f=open("met.jpg", "rb")
data=f.read(10)
if data[6:11] in [b"JFIF",b"Exif"]:
    print("Bu dosya JPEG!")
else:
    print("Bu dosya JPEG değildir!")
print(f.read(10))