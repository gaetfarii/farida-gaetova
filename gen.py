
def prime_number(limit):
    n = 1
    p = False
    while n != limit:
        for i in range(2, n+1):
            if n % i == 0:
                p = False
                if n == i:
                    p = True
                break
        if p:
            yield n
            n += 1
        else:
            n += 1

for a in prime_number(20):
    print(a)



