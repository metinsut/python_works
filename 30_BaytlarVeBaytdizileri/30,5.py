for i in dir(bytes):
    if i not in dir(str):
        print(i)