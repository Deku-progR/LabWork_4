
# name: weight and value
data = {
    'r': (3, 25),
    'p': (2, 15),
    'a': (2, 15),
    'm': (2, 20),
    'i': (1, 5),
    'k': (1, 15),
    'x': (3, 20),
    't': (1, 25),
    'f': (1, 15),
    'd': (1, 10),
    's': (2, 20),
    'c': (2, 20)
}

rows = 2
colomns = 4
# rucksack = [[] for i in range(colomns)] for i in range(rows)]
capacity = rows*colomns
start_points = 20
# disease - паранойя -> антидот d

# print(rucksack)

# Обязательный предмет d
req_size, req_value = data['d']
remaining_capacity = capacity - req_size
# Остальные предметы
other_items = [
    (name,weight,value) for name, (weight,value) in data.items() if name != 'd'
]
# Динамич таблица: в каждой ячейке (очки, список предметов)
table = [
    [(0, []) for w in range(remaining_capacity + 1)]
    for i in range(len(other_items) + 1)
]

for i in range(1,len(other_items)+1):
    name, weight, value = other_items[i-1]
    for w in range(1,remaining_capacity+1):
        # Не взяли предмет
        table[i][w] = table[i-1][w]
        # Берём его, если помещается
        if weight <= w:
            previous_value, previous_name = table[i-1][w-weight]
            take = (previous_value + value, previous_name + [name])
            if take[0] > table[i][w][0]:
                table[i][w] = take

best_value, chosen = table[len(other_items)][remaining_capacity]
# print(best_value,chosen)        
 
# Добавляем обязательный предмет
chosen = chosen + ['d']
best_value += req_value

# chosen_size = sum(data[name][0] for name in chosen)

# Считаем итоговые очки
total_value = sum(value for weight, value in data.values())
final_points = start_points - total_value + 2 * best_value  # добавим ценность 2жды, т.к. её не отнимем, а прибавим

# Создаём инвентарь
rucksack = [[''] * colomns for i in range(rows)]
position = 0
for name in chosen:
    weight, value = data[name]

    for j in range(weight):
        row = position // colomns
        col = position % colomns

        rucksack[row][col] = name
        position += 1

# Вывод результатов
print("Выбранные предметы:", chosen)

print("Инвентарь:")
for row in rucksack:
    print(' '.join(f'[{item}]' for item in row))

print("Итоговые очки выживания:", final_points)

if final_points > 0:
    print("Том выжил!")
else:
    print("Том не выжил!")