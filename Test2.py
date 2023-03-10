"""2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать, вновь выполнить замеры и
ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться"""

from memory_profiler import profile

"""Первое задание. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Первый способ
решается при помощи циклов. Второй способ: при помощи встроенной функции sorted."""


@profile
def f1():
    x = int(input("Введите целое положительное число: "))
    max_num = 0
    y = 0
    while x > 0:
        y = x % 10
        if y > max_num:
            max_num = y
        x //= 10

    print(f"Самая большая цифра числа: {max_num}")
f1()

@profile()

def f2():
    x = int(input("Введите целое положительное число: "))
    return int(sorted(str(x))[-1])
print(f"Самая большая цифра числа: {f2()}")

"""Улучшить выделение памяти не удалось, Вычисление с помощью циклов и
встроенной функции sorted требует одинаковый объем памяти"""

"""Второе задание. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Первый способ: возведение в степень с помощью оператора **. Второй: с использованием цикла."""

@profile()

def exp_func1():
    x = int(input("Введите целое положительное число: "))
    y = int(input("Введите целое отрицательное число: "))
    return x ** y

print(f"Результат {exp_func1()}")

@profile()

def exp_func2():
    x = int(input("Введите целое положительное число: "))
    y = int(input("Введите целое отрицательное число: "))
    result = 1
    for i in range(abs(y)):
        result = result / x
    return result

print(f"Результат {exp_func2()}")

"""Улучшить выделение памяти не удалось, Вычисление с помощью оператора ** и
цикла for требует одинаковый объем памяти"""

"""Третье задание. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится 
месяц (зима, весна, лето, осень). Первый способ: через list, второй: через dict."""

@profile()
def season1():
    month_num = int(input("Введите число от 1 до 12: "))
    seasons_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
    for seasons, months in seasons_dict.items():
        if month_num in months:
            print(f'Время года - {seasons}.')
season1()

@profile()
def season2():
    month_num = int(input("Введите число от 1 до 12: "))
    seasons_list = ['Зима', 1, 'Зима', 2, 'Весна', 3, 'Весна', 4, 'Весна', 5, 'Лето', 6, 'Лето', 7, 'Лето', 8, 'Осень', 9, 'Осень', 10, 'Осень', 11, 'Зима', 12]
    i = seasons_list.index(month_num)
    print(f'Время года - {seasons_list[i - 1]}')
season2()

"""Здесь также улучшить выделение памяти не удалось, Вычисление через list и через dict требует одинаковый объем памятb/
Проанализировав результаты, я сделала вывод, что для данных программ требуется незначительная память по сравнению с 
декоратором @profile. Поэтому измерения стоит делать в более объемных программах либо увеличить точность измерений."""