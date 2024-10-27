#1
"""
def name_age():
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")
    return f"Привіт {name}, тобі {age}!"


print(name_age())

"""
#2
"""
def age():
    age1 = int(input("Введіть ваш вік: "))
    if age1 > 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")


age()
"""

#3
"""
import random


def guess_number():
    number = random.randint(1, 10)
    attempt = 3

    print("Вгадайте число від 1 до 10.")

    while attempt > 0:
        guess = int(input("Введіть число: "))

        if guess == number:
            print("Ви вгадали!")
            break
        elif guess < number:
            print("Більше")
        else:
            print("Менше")

        attempt -= 1

    if attempt == 0:
        print(f"Ви програли. Загадане число було: {number}")


guess_number()
"""
#4
"""
def num():
    for i in range(5, 11):
        print(i)


num()

"""
#6
def factorial(n):
    if n < 0:
        return "Факторіал для від'ємних чисел не визначений."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input("Введіть число n: "))
print(f"Факторіал {n}! = {factorial(n)}")






