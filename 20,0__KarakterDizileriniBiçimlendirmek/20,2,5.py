for sıra,karakter in enumerate(dir(str)):
    if sıra%3==0:
        print("\n",end="")
    print("{:<20}".format(karakter), end="")