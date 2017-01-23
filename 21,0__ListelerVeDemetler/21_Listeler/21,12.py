li1=["elma","armut","erik"]

li2=li1+["karpuz"]
print(li2,li1)

li1[0]="nar"
li2[1]="üzüm"
print(li2,li1)

li2=li1[:]
li2[0]="muz"
print(li2)
print(li1)