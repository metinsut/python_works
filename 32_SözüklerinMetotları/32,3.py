sözlük={'b': 1,
        'c': 2,
        'a': 0,
        'd': 3}


print(sözlük.items())


for sol, sağ in sözlük.items():
    print("{} = {}".format(sol,sağ))