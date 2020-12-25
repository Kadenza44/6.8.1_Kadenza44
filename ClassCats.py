class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

# Метод для вывода параметров отдельно одного кота
    def print_cat(self):
        age_word = None
        if self.age == 1:  # Склоняем слово "год" в зависимости от возраста
            age_word = 'год'
        elif 2 <= self.age <= 4:
            age_word = 'года'
        elif self.age >= 5:
            age_word = 'лет'
        print()  # Пустая строка

        print("Кличка: " + self.name, "\n" "Пол: " + self.sex,"\n" "Возраст: " + str(self.age) + " " + age_word)


