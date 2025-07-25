class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fn(self):
        print(f'Имя: {self.first_name}')

    def ln(self):
        print(f'Фамилия: {self.last_name}')

    def fln(self):
        print(f'Полное имя: {self.first_name} {self.last_name}')
