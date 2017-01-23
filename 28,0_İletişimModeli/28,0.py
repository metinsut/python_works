for i in range(10):
    print(bin(i)[2:].zfill(8))


for i in range(256):
    print(bin(i)[2:],i.bit_length(),sep="\t")










