import time

n = input('Придумайте имя: ')

class Tamagochi:
    def __init__(self):
        self.name = n
        self.hunger = 100
        self.health = 100


new_tamagochi = Tamagochi()


def print_tamagochi(self):
    print('Имя: ', self.name)
    print('Сытость: ', self.hunger)
    print('Здоровье: ', self.health)

def hunger_tamagochi(self):
    if self.hunger != 0:
        self.hunger -= 10

def health_tamagochi(self):
    if self.hunger == 0:
        self.health -= 10
    if self.health == 0:
        print('Тамагочи умер((((')

def feed_tamagochi(self):
    if self.hunger < 100 and self.health != 0:
        k = input('Чтобы покормить нажмите f: ')
        if k == 'f':
            self.hunger += 10

print_tamagochi(new_tamagochi)

while new_tamagochi.health != 0:
    time.sleep(1)
    hunger_tamagochi(new_tamagochi)
    health_tamagochi(new_tamagochi)
    if new_tamagochi.hunger <= 50:  # доп условие
        feed_tamagochi(new_tamagochi)
    print_tamagochi(new_tamagochi)

