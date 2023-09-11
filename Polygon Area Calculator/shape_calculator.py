import math
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) +", height=" + str(self.height) + ")"

    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += "*"
            string += "\n"
        return string

    def set_width(self, num):
        self.width = num

    def set_height(self, num):
        self.height = num

    def get_amount_inside(self, shape):
        return math.floor(((self.get_area()/shape.get_area())))


class Square(Rectangle):

    def __init__(self, width):
        self.width = width
        self.height = width

    def set_side(self, num):
        self.width = num
        self.height = num

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"