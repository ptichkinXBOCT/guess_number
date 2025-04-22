class Product:
    def __init__(self, product_name, product_count) -> None:
        self.product_name = product_name
        self.product_count = product_count

    def get_info(self):
        return f'{self.product_name} (в наличии: {self.product_count})'


class Kettlebell(Product):
    def __init__(self, product_name, product_count, weight) -> None:
        super().__init__(product_name, product_count)
        self.weight = weight

    def get_weight(self):
        return f'{self.get_info()}. Вес: {self.weight} кг'


class Clothing(Product):
    def __init__(self, product_name, product_count, size) -> None:
        super().__init__(product_name, product_count)
        self.size = size

    def get_size(self):
        return f'{self.get_info()}. Размер: {self.size}'


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
