class Çalışan():
    kabiliyetleri = ['sınıf niteliği']

    def __init__(self):
        self.kabiliyetleri = ['örnek niteliği']



ahmet=Çalışan()
mehmet=Çalışan()
print(ahmet.kabiliyetleri)
print(Çalışan.kabiliyetleri)
ahmet.kabiliyetleri.append(25)
print(mehmet.kabiliyetleri)
print(ahmet.kabiliyetleri)







