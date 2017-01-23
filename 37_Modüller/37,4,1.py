import sözlük
import sys
from distutils import sysconfig


print(sözlük)

print(sys.path)

print(sysconfig.get_python_lib())

print(dir(sözlük))


print(sözlük.sözlük)
print(sys.version)
print(sözlük.ara("kitap"))


print(sözlük.ekle("kapı","door"))
print(sözlük.sözlük)

print(sözlük.ekle("one","bir"))
print(sözlük.sözlük)


print(sözlük.sil("one"))
print(sözlük.sil("kitap"))
print(sözlük.sil("computer"))


print(sözlük.sözlük)


