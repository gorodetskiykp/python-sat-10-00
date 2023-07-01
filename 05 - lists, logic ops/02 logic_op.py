number1 = 9
number2 = 0

# Тип данных bool - True/False - 1/0

print(1 + 1 + 1)
print(True + True + True)

print(number1 > number2)  # True
print(number1 < number2)  # False
print(number1 >= number2)  # True
print(number1 <= number2)  # False
print(number1 == number2)  # False ('==')
print(number1 != number2)  # True ('! =')
print(number2 < 4 < number1)  # True

print('hello' in 'hello world')  # True
print('hello' not in 'hello world')  # False

number1_1 = 9
print(number1 is number1_1)  # True

number3 = 12_256
number3_1 = 12_256
print(number3 is number3_1)

print(id(number3))
print(id(number3_1))

number3_2 = (12_255 + 1) * 100_000
print(number3_2)
print(id(number3_2))

number3_3 = 1_225_600_000
print(number3_3)
print(id(number3_3))

# == - проверяет равенство значений
# is - проверяет совпадение значений + адресов памяти

print()
print(id('hell' + 'o'))
print(id('hello'))

# сравнение строк
# ord('a') - порядковый номер в таблице символов (cp1251, windows-1251, utf-8, ascii)

print(ord('a'))
print(ord('b'))
print(ord('A'))

print('a' > 'A')  # True -> 97 > 65
print('aaa' > 'aAz')  # True -> 97 > 65 (посимвольное сравнение)

# Открыть холодильник
# Проверить количество яиц
# Если яиц меньше 2 - выпить кофе или чай
# Если яиц хотя бы 2
# Проверить молоко
# Если молоко есть - сделать омлет
# Если молока нет - сделать яичницу
eggs = 2
milk = True
coffee = True
tea = True

print((eggs >= 2) and (milk == True))  # омлет
print(eggs >= 2 and milk == False)  # яичница
print(eggs < 2)  # кофе

print(coffee == True or tea == True)  # True

# op1   | op2   | and   | or
# True  | True  | True  | True
# True  | False | False | True
# False | True  | False | True
# False | False | False | False
