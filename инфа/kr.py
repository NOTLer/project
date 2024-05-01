class Pair:
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def get_first(self):
        return self._first

    def set_first(self, value):
        self._first = value

    def get_second(self):
        return self._second

    def set_second(self, value):
        self._second = value

    def increase(self, value):
        self._first += value
        self._second += value


class Fraction:
    def __init__(self, first, second):
        self.pair = Pair(first, second)

    def write(self, file_name):
        with open(file_name, "a") as file:
            file.write(f"{self.pair.get_first()} / {self.pair.get_second()}\n")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.pair.get_first() * other.pair.get_first(),
                            self.pair.get_second() * other.pair.get_second())
        elif isinstance(other, (int, float)):
            return Fraction(self.pair.get_first() * other,
                            self.pair.get_second() * other)
        else:
            raise TypeError("Unsupported operand type for multiplication")

    def __str__(self):
        return f"{self.pair.get_first()} / {self.pair.get_second()}"


# Чтение дробей из файла
def read_fractions(file_name):
    fractions = []
    with open(file_name, "r") as file:
        for line in file:
            first, second = map(int, line.strip().split("/"))
            fractions.append(Fraction(first, second))
    return fractions


# Главная программа
def main():
    f1 = Fraction(3, 6)
    f2 = Fraction(1, 4)
    f1.write("new.txt")
    f2.write("new.txt")
    # Создание списка дробей на основе данных из файла
    fractions = read_fractions("new.txt")

    # Вывод исходных дробей
    print("Исходные дроби:")
    for fraction in fractions:
        print(fraction)

    # Умножение дробей на число
    multiplied_fractions = [fraction * 5 for fraction in fractions]

    # Вывод и запись новых дробей
    print("\nНовые дроби:")
    for fraction in multiplied_fractions:
        print(fraction)
        fraction.write("new.txt")


if __name__ == "__main__":
    main()
