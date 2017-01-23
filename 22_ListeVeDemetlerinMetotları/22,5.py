meyveler = ["elma", "armut", "çilek", "kiraz"]
print(meyveler[::-1])
print(*reversed(meyveler))

print(list(reversed(meyveler)))
for i in reversed(meyveler):
    print(i)
print(meyveler.reverse())

