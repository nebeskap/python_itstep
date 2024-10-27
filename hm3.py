class Rectangle:
    def __init__(self, width = 4, height = 12):
        self.width = width
        self.height = height

    def calculate_area(self):
        print("S Rectangle=", self.width*self.height)


    def calculate_perimetr(self):
        print("P Rectangle=", (self.width+self.height)*2)


S = Rectangle()
S.calculate_area()
P = Rectangle()
P.calculate_perimetr()