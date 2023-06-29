spaces = ' '
print('Фирма: Рога и копыта')
print(spaces * 61 + 'Дата 10.06.2023г.')
print(spaces * 30 + 'ТОВАРНЫЙ ЧЕК')
print('Наименование товара' + spaces * 12 + 'Кол-во' + spaces * 12 + 'Цена'
      + spaces * 12 + 'Сумма')
print('Белый хлеб' + spaces * 23 + '1' + spaces * 12,
      '25руб. 39коп.' + spaces * 5 + '25руб. 39коп.')
print('Молоко' + spaces * 27 + '1' + spaces * 13 + '81руб. 49коп.',
      spaces * 4 + '81руб. 49коп.')
print('Чай в пакетиках' + spaces * 18 + '1' + spaces * 12 + '139руб. 00коп.',
      spaces * 3 + '139руб. 00коп.')
print('Колбаса' + spaces * 26 + '1' + spaces * 12 + '600руб. 49коп.',
      spaces * 3 + '600руб. 49коп.')
print('Сыр голландский' + spaces * 18 + '1' + spaces * 12 + '459руб. 79коп.',
      spaces * 3 + '459руб. 79коп.')
print('Шоколад' + spaces * 26 + '1' + spaces * 13 + '99руб. 99коп.',
      spaces * 4 + '99руб. 99коп.')
print('Всего: 1406руб. 15коп.')
print(spaces * 50 + 'Подпись продавца: ')


# Использование """
print("""
Фирма: Рога и копыта
                                                             Дата 10.06.2023г.
                              ТОВАРНЫЙ ЧЕК
Наименование товара            Кол-во              Цена              Сумма
Белый хлеб                       1             25руб. 39коп.     25руб. 39коп.
Молоко                           1             81руб. 49коп.     81руб. 49коп.
Чай в пакетиках                  1            139руб. 00коп.    139руб. 00коп.
Колбаса                          1            600руб. 49коп.    600руб. 49коп.
Сыр голландский                  1            459руб. 79коп.    459руб. 79коп.
Шоколад                          1             99руб. 99коп.     99руб. 99коп.
Всего: 1406руб. 15коп.
                                                  Подпись продавца: __________

""")


# Использование переменных
date = '10.06.2023 г'
item1 = 'Белый хлеб '
item2 = 'Молоко'
item3 = 'Чай в пакетиках'
item4 = 'Колбаса'
item5 = 'Сыр голландский'
item6 = 'Шоколад'
count1 = 1
count2 = 3
count3 = 1
count4 = 4
count5 = 1
count6 = 2
price1 = 25.39
price2 = 81.49
price3 = 139.5
price4 = 600.49
price5 = 459.9
price6 = 99.99
total1 = count1 * price1
total2 = count2 * price2
total3 = count3 * price3
total4 = count4 * price4
total5 = count5 * price5
total6 = count6 * price6
total_price = total1 + total2 + total3 + total4 + total5 + total6

print('Фирма: Рога и копыта')
print('Дата', date)
print('ТОВАРНЫЙ ЧЕК')
print('Наименование товара', 'Кол-во', 'Цена', 'Сумма')
print(item1, count1, price1, total1)
print(item2, count2, price2, total2)
print(item3, count3, price3, total3)
print(item4, count4, price4, total4)
print(item5, count5, price5, total5)
print(item6, count6, price6, total6)
print('Всего:', total_price)
print('Подпись продавца:')


# использование .format()
# 'Привет! Меня зовут {}'.format('Иван')  # Привет! Меня зовут Иван
print('Фирма: Рога и копыта')
print('{:>60}'.format('Дата ' + date))
print('{:^60}'.format('ТОВАРНЫЙ ЧЕК'))
print('{:^25}{:^5}{:^10}{:^20}'.format('Наименование товара', 'Кол-во', 'Цена',
                                       'Сумма'))
print('{:<25}{:^5}{:>10}{:>20.2f}'.format(item1, count1, price1, total1))
print('{:<25}{:^5}{:>10}{:>20.2f}'.format(item2, count2, price2, total2))
print('{:<25}{:^5}{:>10}{:>20.2f}'.format(item3, count3, price3, total3))
print('{:<25}{:^5}{:>10}{:>20.2f}'.format(item4, count4, price4, total4))
print('{:<25}{:^5}{:>10}{:>20.2f}'.format(item5, count5, price5, total5))
print('{:<25}{:^5}{:>10}{:>20.2f}'.format(item6, count6, price6, total6))
print('{:<40}{:>20.2f}'.format('Всего:',  total_price))
print('{:>50}{:10}'.format('Подпись продавца:', '_' * 10))
