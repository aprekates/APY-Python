a = []
for i in range(0,3):
    a.append( [ ] )
    for j in range(0,3):
        a[i].append(0)

print a
a[1][0] = 44
a[1][1] = 55
a[1][2] = 66
print a
print a[0]
print a[1]
print a[0][2]
