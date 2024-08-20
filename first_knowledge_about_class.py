class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, spend_days):
        self.remaining_vacation_days -= spend_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


employee3 = Employee('Мария', 'Эрих', 'м')
employee3.consume_vacation(7)
employee3.consume_vacation(1)
print(employee3.get_vacation_details())


# print(employee3.vacation_days)

'''
employee1 = Employee('Роберт', 'Крузо', 'м')
employee2 = Employee('Густав', 'Климт', 'м')

print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, '
      f'Пол: {employee1.gender}, '
      f'Отпускных дней в году: {employee1.vacation_days}.')
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, '
      f'Пол: {employee2.gender}, '
      f'Отпускных дней в году: {employee2.vacation_days}.')
'''
