n = int(input())
ans = False
a = 0
for i in range(n):
    g = int(input())
    t = list(str(g))
    c = 0
    if int(t[0]) % 2 == 0:
        for x in range(len(t)):
            if int(t[x]) % 2 == 0:
                c += 1
    else:
        for x in range(len(t)):
            if int(t[x]) % 2 != 0:
                c += 1

    if len(t) == c == 3 or len(t) == c == 5:
        a += 1

if a == 2:
    ans = True
print(ans)
