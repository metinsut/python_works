meyve="elma"

print("E"+meyve[1:])

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for i in site1,site2,site3,site4:
    print("http://"+i)

for i in site1,site2,site3,site4:
    print("http//:"+i[4:])