with open("liste.txt","r+") as f:
    f.readline()
    f.seek(f.tell())
    f.truncate()