#Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
#возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
#необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора *.
#Второй — более сложная реализация без оператора *, предусматривающая использование цикла.

# Возведение в степень с помощью оператора *.

x = int(input("Введите целое положительное число: "))
y = int(input("Введите целое отрицательное число: "))

def exp_func1(x, y):
    return x ** y
print(f"Возведение {x} в степень {y} с оператором '**' c результатом {exp_func1(x, y)}")

# Реализация без оператора *, предусматривающая использование цикла.

def exp_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result = result / x
    return result

print(f"Возведение {x} в степень {y} с использованием цикла с результатом {exp_func2(x, y)}")