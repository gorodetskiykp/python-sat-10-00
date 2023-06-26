count = 5  # в count помещается адрес ячейки памяти, в которой находится число 5

print(id(count))
print(count)

new_count = count

print(id(count))
print(id(new_count))

print('count = 10')
count = 1000
print(id(count))
print(id(new_count))

new_count = 7

# int, str - неизменяемые типы
