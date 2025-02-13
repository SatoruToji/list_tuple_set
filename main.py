l = [1, 2, 3, 'privet', 23, 34, 34, 34] # The List
t = (1, 2, 3, 'privet', 23, 34, 34, 34) # The Tuple
s = {1, 2, 3, 'privet', 23, 34, 34, 34} # The Set


# Порядок элементов:
print(
    type(l), ':', l, '\n', # Сохраняет
    type(t), ':', t, '\n', # Сохраняет 
    type(s), ':', s  # Не сохраняет (перемешивает порядок элементов) + удаляет дупликаты
)


# Изменяемость:

# List
l1 = ['EXTEND', 'EXTEND']
print(l)

l.append('xd')                                                                      # Добавляет эл. в конец списка
l.insert(1, 'INSERT')                                                           # Добавляет эл. в указанный index
l.extend(l1)                                                                          # Склеивает два списка в единый
l.remove(3)                                                                          # Удаляет эл. по указанному значению (не по index)
print('Возврат удаленного элемента: ', l.pop(2))               # Сначало возвращает, потом удаляет эл. по указанному index
print('Колличество эл. "34": ', l.count(34))                       # Возвращает колличество одинаковых Элементов.

print(l)

# Tuple
print(t)

print('Эл. под индексом 3:',t[3])                                       # Только поиск по индексам


# Set почти такой же как List, НО... 
# Во-первых, set не хранит дубликаты эл
# Во-вторых set постоянно меняет порядок хранения Эл.
# В-третих, индексация или поиск по индексу не работает (иза хаоса порядка)

try:
    s[2]
except:
    print('fcku')
    
# Ну и В-четвертых... в Set нельзя добавить List в качестве Эл. (любые другие изменяемые объекты).

# Примеры использования: 

# LIST
print('List - когда тебе необходимо изменять данные: удалять, добавлять, копировать')

# TUPLE
print('Tuple - неизменяемый как почти CONST,  занимает меньше памяти')

# SET
print(
    'Set - позволяет быстро проверить наличие Эл. (x in set), сам удаляет дупликаты'
    )