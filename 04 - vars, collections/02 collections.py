# список - list
items = [
    'Хлеб',
    'Молоко',
    'Сыр',
    'Сок',
]
counts = [1, 2, 1, 1]

'Молоко'[0]  # 'М'
print(items)
single_item = items[1]  # 'Молоко'
items[1] = 'Молоко 3.2%'
print(items)
single_item_count = items[1]  # 2


# кортеж - tuple
items = (
    'Хлеб',
    'Молоко',
    'Сыр',
    'Сок',
)
counts = (1, 2, 1, 1)
# counts = 1, 2, 1, 1

print(items)
single_item = items[1]  # 'Молоко'
# items[1] = 'Молоко 3.2%'  - TypeError: 'tuple' object does not support item assignment
print(items)
single_item_count = items[1]  # 2


single_item_tuple = (10, )
print(type(single_item_tuple))

print(   (1, 2, 3, 4)    )
