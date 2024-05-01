import random as r

class Animal():
    def __init__(self, name):
        self._name = name
        print(f"Появился {self._name}")

    def get_name(self):
        print(self._name)

    def animal_move(self):
        print("Оно передвигается!")

    def eating(self):
        print(self._name + " кушает")

    


class insects(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.animal_class = "Насекомое"
        print("Класса " + self.animal_class)

    def reproducting_by_insects(self):
        print(self.animal_class + "откладывает яйца")


class spider(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name)
        self.age = age
        self.breed = breed

    def get_info(self):
        print(self.age)
        print(self._name)
        print(self.breed)

    def eating(self):
        print(self._name + " охотиться")


class Mammalia(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.animal_class = "Млекопитающие"
        print(self._name + " из класса " + self.animal_class)

    def reproducting_by_mammalia(self):
        print(self.animal_class + "размножается")


class Horse(Mammalia):
    def __init__(self, name, age, breed):
        super().__init__(name)
        self.age = age
        self.breed = breed

    def get_info(self):
        print(self.age)
        print(self._name)
        print(self.breed)

    def run(self):
        print("Бежит трусцой")


class Dog(Mammalia):
    def __init__(self, name, age, breed):
        super().__init__(name)
        self.age = age
        self.breed = breed

    def get_info(self):
        print(self.age)
        print(self._name)
        print(self.breed)

    def golos(self):
        print("Гав!")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.animal_class = "Рыба"
        print(self._name + " из класса " + self.animal_class)

    def reproducting_by_mammalia(self):
        print(self.animal_class + " откладывает икру")


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.animal_class = "Хищник"
        print(self._name + " из класса " + self.animal_class)

    def reproducting_by_mammalia(self):
        print(self.animal_class + " размножается")

    def hunt(self):
        print(self.animal_class + " охотится")


class Crocodile(Predator):

    def __init__(self, name, age, breed):
        super().__init__(name)
        self.age = age
        self.breed = breed

    def get_info(self):
        print(self.age)
        print(self._name)
        print(self.breed)


def skachki(list_of_hourse):
	if len(list_of_hourse) >= 2:
		print(list_of_hourse[r.randint(0, len(list_of_hourse) - 1)])
		

horse1 = Horse("Кузя", 10, "пятнистый")
horse2 = Horse("Лунтик", 8, "белый")
skachki([horse1, horse2])
# horse.eating()
# horse.animal_move()
# horse.run()
# horse.get_info()
