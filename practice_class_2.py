class MushroomsCollector:
    # Инициализация, где корзина для каждого экземпляра класса своя
    def __init__(self):
        self.mushrooms = []

    def is_poisonous(self, mushroom_name):
        if mushroom_name in ['Мухомор', 'Поганка']:
            return True
        else:
            return False

    # Допишите метод.
    def add_mushroom(self, mushroom_name):
        if not self.is_poisonous(mushroom_name):
            self.mushrooms.append(mushroom_name)
        else:
            print('Нельзя добавить ядовитый гриб')

    def __str__(self):
        return str.join(', ', self.mushrooms)


# Пример запуска для самопроверки
collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)
print(collector_2)
