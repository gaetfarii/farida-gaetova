# 3

a = int(input())
b = list(str(a))
n = len(b)-1
s = int(b[len(b)-1])

while n != -1:
    if n % 2 != 0:
        s -= int(b[n])
    else:
        s += int(b[n])
    n -= 1

print(s)


# 4
num = int(input())
print(len(str(num)))



# 5

num = int(input())
l = list((str(num)))
s = 0
for i in range(len(l)):
    if int(l[i]) % 2 != 0:
        s = s * 10 + int(l[i])
print(s)

# 6

num = int(input())
l = list(str(num))
s = 1
for i in range(len(l)):
    s = s * 10 + int(l[i])
s = s * 10 + 1
print(s)

# 7
num = int(input())
print(max(list(str(num))))

# 8
n = int(input())
x = 0
for i in range(n):
    t = 1
    for g in range(i):
        t = t * 10 + 1
    x += t
print(x)
