# класс ввели как контейнер для удобства. self - имя объекта, кот-ый принадлежит классу. Ключевое - обращамся словами, а не по индексу. Более читаемо
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def knapsack(items, capacity):
    # СЕМАФОР 
    def node_bound_count(i, weight, value):
        if weight > capacity:  # Отсекли ветвь, если она не лезет в рюкзак
            return 0
        # Переводим полученные переменные в область локальных переменных
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:  # Ветвь нового предмета, если его можно положить по весу и
            # такой эл-т в целом есть
            node_value += items[j].value  # Прибавляем ценность текущ предмета
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            # Здесь просто формула. Расчёт того, насколько 
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)
        # расчёт текущ. узла
        return node_value
    
    def branch_bound(i, weight, value):
        # Чтобы изменять внешнюю max_value
        nonlocal max_value
        # Берём оптимальный вариант ценности
        if weight <= capacity and value > max_value:
            max_value = value
        # Достигли конца текущ. дерева
        if i == len(items):
            return 0
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i+1, weight, value)
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            branch_bound(i+1, weight + items[i].weight, value + items[i].value)

    # Возвращаем перевёрнутым.
    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    branch_bound(0, 0, 0)
    return max_value


if __name__ == '__main__':
    items = [Item(3, 700), Item(1, 300), Item(2, 500),
             Item(2, 550), Item(3, 800)]
    capacity = 4
    max_value = knapsack(items, capacity)
    print(max_value)