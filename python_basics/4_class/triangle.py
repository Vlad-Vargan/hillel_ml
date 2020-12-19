# Створити клас для роботи з трикутниками.
# Форму представлення і допустимі операції вибрати самостійно.


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    
    def perimetr(self):
        triangle_perimetr = self.side_1 + self.side_2 + self.side_3
        return triangle_perimetr
    
    def area(self):
        s = self.perimetr() / 2
        triangle_area = (
                s * (s-self.side_1) * (s-self.side_2) * (s-self.side_3)
            ) ** 0.5
        triangle_area = round(triangle_area, 2)
        return triangle_area


tr = Triangle(1, 1, 1)
print(tr.perimetr())
print(tr.area())
