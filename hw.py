word_1 = input()  # задача № 4
word_2 = input()
if sorted(word_1) == sorted(word_2):
    print('True')
else:
    print('False')




a = [3, 2, 5, 7, 9]  # задача №5
a1 = 0
for i in range(len(a)):
    a1 = a1 + a[i] * 10 ** (len(a) - i - 1)
a1 = a1 + 1
b = [int(n) for n in str(a1)]
print(b)



a = [23, 56, 81, 94, 66, 20]  # задача № 6
b = 86
for i in range(len(a)):
    for n in range(i + 1, len(a)):
        if a[i] + a[n] == b:
            print(a[i], a[n])



a = input()  # задача № 7
print(a[::-1])



a = input()  # задача № 8
def palindrome(data):
    data = data.replace(' ', '').lower()
    data = data.replace(',', '').lower()
    data = data.replace('.', '').lower()
    data = data.replace('!', '').lower()
    data = data.replace('?', '').lower()
    print(data)
    if data == data[::-1]:
        return True
    else:
        return False
print(palindrome(a))
