"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.

Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
import random
x = int (random.randint(1, 1000))
y = int (random.randint(1, 1000))

sum = x+y  # сумму загадоных чисел
mult = x*y  # произведение загаданных чисел

print(f'сумму загадоных чисел = {sum} а произведение этих чисел = {mult}')
# Помощь Кате
for i in range(1, 1001):
    for j in range(1, 1001):
        if i+j == sum and i*j == mult:
            print(f'загаданное число: {i}')