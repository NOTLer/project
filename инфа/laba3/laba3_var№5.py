import abc
import math


class Body(abc.ABC):
    @abc.abstractmethod
    def volume(self):
        pass

    @abc.abstractmethod
    def square(self):
        pass


class Parallelepiped(Body):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def square(self):
        return 2 * (self.x * self.y + self.x * self.z + self.y * self.z)

    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z}), Volume={self.volume()}, Square={self.square()}"


class Cone(Body):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        return self.r * self.r * self.h * math.pi / 3

    def square(self):
        return math.pi * self.r * (self.r + math.sqrt(self.h * self.h + self.r * self.r))

    def __str__(self):
        return f"{self.__class__.__name__}(r={self.r}, h={self.h}), Volume={self.volume()}, Square={self.square()}"


class Ball(Body):
    def __init__(self, r):
        self.r = r

    def volume(self):
        return 4 / 3 * math.pi * self.r ** 3

    def square(self):
        return 4 * math.pi * self.r ** 2

    def __str__(self):
        return f"{self.__class__.__name__}(r={self.r}), Volume={self.volume()}, Square={self.square()}"


class Series:
    def __init__(self):
        self.list = []

    def append(self, obj):
        self.list.append(obj)

    def __str__(self):
        result = ""
        for obj in self.list:
            result += str(obj) + "\n"
        return result

# это доб задание !!! 
class Cube(Parallelepiped):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side, side)
        


# main
ball1 = Ball(2)
ball2 = Ball(3)
cube1 = Cube(2)

ser = Series()
ser.append(ball1)
ser.append(ball2)
ser.append(cube1)

print(ser)
