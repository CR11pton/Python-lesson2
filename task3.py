# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

Number = int(input('Введите число: '))
i = 1
while i <= Number:
    print(i)
    if i // 2:
        i *= 2
    else:
        i += 1