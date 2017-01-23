for sıra,karakter in enumerate(dir(str)):
    if sıra%3==0:
        print("\n",end="")
    print("%3.3d" %sıra,karakter.ljust(25),end="")


for i in range(20):
    print("%2d%  5o%  5x" %(i, i, i))

