numbers = [1, 2, 3]

print(type(numbers))
print(numbers[0])  # 1
print(numbers[2])  # 3
print(numbers[-1])  # 3

print(numbers[20])  # IndexError: list index out of range

# Доступ к методам объекта
numbers.append('hello')  # добавить элемент в конец списка
print(numbers)
numbers[-1] = 'HELLO'
print(numbers)

numbers.insert(1, 'FIRST')  # добавить элемент на определенную позицию
print(numbers)

numbers.pop()  # удалить элемент в конеце списка
print(numbers)

numbers.pop(1)  # удалить элемент c определенной позиции
print(numbers)

numbers.append(1)
print(numbers)

numbers.remove(1)  # удалить элемент со значением 1 (первый попавшийся слева)
print(numbers)

# строки - неизменяемые типы данных
word = 'hello world'
print(word)
word_up = word.upper()  # возвращает строку в верхнем регистре
print(word)
print(word_up)

# dir() - возвращает список всех свойств и методов объекта
