from datetime import datetime

def count_time(f):
    def time(s):
        start = datetime.now()
        file = open('decorators.txt', 'w', encoding='utf-8' )
        done = f(s)
        end = datetime.now()
        s = '\n'
        file.write(f'Вызвана в {start}{s}Завершена в {end}{s}Выполнялась {end - start} секунд')
        return done
    return time

@count_time
def fact(n):
    a = 1
    b = []
    for i in range(n):
        a = a*(i+1)
        b.append(a)
    return b

fact(1000)