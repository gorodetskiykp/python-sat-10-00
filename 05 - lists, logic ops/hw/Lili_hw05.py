date = '29.06.2023 г.'
check_number = '№205'
goods = ['Газета "Деловой Петербург"', 'Ручка шариковая',
         'Книга о вкусной и здоровой пищи', 'Газета "Пионер"']
counts = [1, 3, 2, 1]
prices = [10, 8, 30, 13]

new_good = input('Введите новый товар: ')
new_counts = input('Введите количество этого товара: ')
new_prices = input('Введите цену этого товара: ')

goods.append(new_good)
counts.append(int(new_counts))
prices.append(int(new_prices))

totals = [counts[0] * prices[0], counts[1] * prices[1], counts[2] * prices[2],
          counts[3] * prices[3], counts[4] * prices[4]]
summ = totals[0] + totals[1] + totals[2] + totals[3] + totals[4]
name = 'Иванова Мария'

print('ИП Онегин г. Санкт-Петербург, пр. Невский, д.5')
print('{:>100}'.format('Дата ' + date))
print('{:>50}{:<50}'.format('ТОВАРНЫЙ ЧЕК ', check_number))
print('{:^55}{:^10}{:^15}{:^20}'.format('Наименование товара', 'Кол-во',
                                        'Цена', 'Сумма'))
print('{:<55}{:^10}{:^15}{:^20}'.format(
    goods[0],
    counts[0],
    prices[0],
    totals[0]
))
print('{:<55}{:^10}{:^15}{:^20}'.format(
    goods[1],
    counts[1],
    prices[1],
    totals[1]))
print('{:<55}{:^10}{:^15}{:^20}'.format(
    goods[2],
    counts[2],
    prices[2],
    totals[2]))
print('{:<55}{:^10}{:^15}{:^20}'.format(
    goods[3],
    counts[3],
    prices[3],
    totals[3],
))
print('{:<55}{:^10}{:^15}{:^20}'.format(
    goods[4],
    counts[4],
    prices[4],
    totals[4],
))
print('{:<10}{:<90}'.format('Итого:', summ))
print(
    '{:<10}{:<40}{:<10}{:<40}'.format('Продавец:', name, 'Подпись:', '_' * 10))
