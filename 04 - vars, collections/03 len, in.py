# Последовательности

# str
# list
# tuple

ex_str = "Hello"
ex_list = [1, 2, 3, 4, "Hello", [1, 2, 3]]
ex_tuple = (1, 2, 3, 4, "Hello")

# 1. Всегда можно подсчитать кол-во элементов - len()
print(len(ex_str))  # 5
print(len(ex_list)) # 6
print(len(ex_tuple))  # 5

# 2. Доступно определение наличия элемена к последовательности - in
print('e' in ex_str)  # True
print('5' in ex_list)  # False
print('e' in ex_tuple)  # False

# 3. Можно обратиться к элементу по индексу
print(ex_str[0])  # 'H'
print(ex_list[1])  # 2
print(ex_tuple[2])  # 3
