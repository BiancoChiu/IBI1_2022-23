a = -3.19
b = -118.24
c = 116.39
d = abs(a - b)
e = abs(a - c)
if d > e:
    print('d is greater and LA is further')
elif e > d:
    print('e is greater and Haining is further')
else:
    print('same distance')
# e is greater and Haining is further

X, Y = True, False
W = X and Y
Z = X or Y
print(W, Z)
# False True
