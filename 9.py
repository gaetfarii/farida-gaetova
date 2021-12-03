a = [1, 2, 3, 4, 5]
a2 = [4, 2, 3, 5, 1]
b = [1, 2, 3, 4, 5]
b2 = [2, 1, 4, 3, 5]
c = [1, 2, 3, 4, 5]
c2 = []
for i in range(len(a2)):
    for k in range(len(b)):
        if a2[i] == b[k]:
            c2.insert(i, b2[k])
a2 = c2
print(a, a2)
