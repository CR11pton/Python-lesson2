
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# Пример:
# 5 -> 1 0 1 1 0
# 2

# Решка = Tail
# Герб = Head
from random import randint
coins_number = int(input('How many coins?: '))
Head = 0
Tail = 0
for _ in range(coins_number):
    coin_type = randint(1, 2)
    # print(coin_type)
    if coin_type == 2:
        # print('Tail')
        Tail += 1
    else:
        # print('Head')
        Head += 1
print(f'Coins with head side {Head}')
print(f'Coins with tail side {Tail}')
if Tail > Head:
    print(f'Head needs less: {Head} turns')
else:
    print(f' Tail needs less: {Tail} turns')
