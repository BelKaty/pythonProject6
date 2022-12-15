# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

month_num = int(input("Введите число от 1 до 12: "))

#решение через dict
def season1(month_num):
    seasons_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
    for seasons, months in seasons_dict.items():
        if month_num in months:
            print(f'Время года - {seasons}.')
season1(month_num)

#решение через list
def season2(month_num):
    seasons_list = ['Зима', 1, 'Зима', 2, 'Весна', 3, 'Весна', 4, 'Весна', 5, 'Лето', 6, 'Лето', 7, 'Лето', 8, 'Осень', 9, 'Осень', 10, 'Осень', 11, 'Зима', 12]
    i = seasons_list.index(month_num)
    print(f'Время года - {seasons_list[i - 1]}')
season2(month_num)