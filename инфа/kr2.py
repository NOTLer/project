class Car():
    def __init__(self, marka, num_of_cil, power):
        self.__marka = marka
        self.__num_of_cil = num_of_cil
        self._power = power

    def get_num_of_cil(self):
        return self.__num_of_cil

    def getmark(self):
        return self.__marka

    def setmarka(self, name):
        self.__marka = name

    def print(self):
        print("Это машина ", self.__marka, self.__num_of_cil, self._power)

    def __eq__(self, other):
        if self.__marka == other.__marka:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"({self.__marka}, {self.__num_of_cil}, {self._power})"


class Lorry(Car):
    def __init__(self, marka, num_of_cil, power, carring):
        super().__init__(marka, num_of_cil, power)
        self._carring = carring

    def print(self):
        print("Это грузовик ", self.getmark(), self.get_num_of_cil(), self._power, self._carring)

    def __str__(self) -> str:
        return f"({self.getmark()}, {self.get_num_of_cil()}, {self._power}, {self._carring})"
    
    
#main 

lorry = Lorry("BMW", 6, 500, 30000)
car1 = Car("Mersedes", 6, 400)
car2 = Car("Reno", 4, 600)

lis = [lorry, car1, car2]

def print_list(lis):
    with open("input.txt", "a") as f:
        for i in lis:
            f.write(str(i) + "\n")


def print_123(lis):
    for i in lis:
        i.print()

print_list(lis)
print_123(lis)