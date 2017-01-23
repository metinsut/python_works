l=[400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236,241, 123, 249, 364, 292, 153]

#
# for i in l:
#     if i%2==1:
#         print(i)

# print([i for i in l if i%2==1])


def tek(sayı):
    return sayı%2==1



print(*filter(tek,l))


print(list(filter(tek,l)))






