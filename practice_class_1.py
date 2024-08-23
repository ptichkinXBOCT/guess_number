class BacteriaProducer:
    # Допишите инициализатор класса
    def __init__(self, max_bacteria):
        self.max_bacteria = max_bacteria
        self.count_bacteria = 0

    # Допишите метод
    def create_new(self):
        if self.count_bacteria < self.max_bacteria:
            self.count_bacteria = self.count_bacteria + 1
            print(f'Добавлена одна бактерия. Количество бактерий в популяции: '
                  f'{self.count_bacteria}')
        else:
            print('Нет места под новую бактерию')

    # Допишите метод
    def remove_one(self):
        if self.count_bacteria > 0:
            self.count_bacteria -= 1
            print(f'Одна бактерия удалена. Количество бактерий в популяции: '
                  f'{self.count_bacteria}')
        else:
            print('В популяции нет бактерий, удалять нечего')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
