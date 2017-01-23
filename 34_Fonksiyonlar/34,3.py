def selamla():
    print("Elveda Zalim Dünya!")

def sistem_bilgisi_göster():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tAna sürüm numarası        : ",sys.version_info.major)
    print("\tAlt sürüm numarası        : ", sys.version_info.minor)
    print("\tMinik sürüm numarası      : ", sys.version_info.micro)
    print("\n\tKullanılan işletim sistemi: ",sys.platform)


sistem_bilgisi_göster()