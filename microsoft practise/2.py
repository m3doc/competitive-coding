import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return 3.14*self.radius*self.radius
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width*self.height

class Square:
    def __init__(self, width):
        self.width  = width

    def getArea(self):
        return self.width*self.width


radius = float(raw_input())
c1 = Circle(radius)
print int(math.ceil(c1.getArea()))

dims = raw_input().strip().split(" ")
width = float(dims[0])
height = float(dims[1])

r1  = Rectangle(width,height)
print int(math.ceil(r1.getArea()))

radius = float(raw_input())
c2 = Circle(radius)
print int(math.ceil(c2.getArea()))



width = float(raw_input())
s1 = Square(width)
print int(math.ceil(s1.getArea()))


dims = raw_input().strip().split(" ")
width = float(dims[0])
height = float(dims[1])
r2 = Rectangle(width, height)
print int(math.ceil(r2.getArea()))







