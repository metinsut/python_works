print("Python programlama dili")

a="elma "
print("{} kilo {} kaldı!".format(23, a.strip()))
print("{} kilo {} kaldı!".format(23, a))




print(repr(a))


print(repr("karakter dizisi\n"))
print("karakter dizisi\n")


for i in range(128):
    if i % 4 == 0:
        print("\n")

    print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")