"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""

import random

n = int(input("Введите количество монеток на столе: "))
# Создаем переменые для подсчета сторон из n монет
side1 = 0
side2 = 1
# Проходимся по всем монеткам и записываем в count их сторону
for _ in range(n-1):
    count = random.randint(1, 2)  # случайное определение сторон
    if count == 1:
        side1 += 1
    else:
        count == 2
        side2 += 1
    # print(i)
print(f"Посчитали монеток повернутое вверх решкой {side1}, соответсвенно орлом {side2}")

print('Минимальное количество монет, которые нужно перевернуть')
if side1 < side2:        # Находим минимальное количество перевернутых одной стороной монеток
    print(side1)
else:
    print(side2)
