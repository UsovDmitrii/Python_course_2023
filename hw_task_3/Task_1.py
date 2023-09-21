"""
1.	Создайте класс  прямоугольника. Класс принимает два параметра, ширина и высота прямоугольника.
Создайте два метода:
-	метод возвращающий площадь прямоугольника
-	метод возвращающий периметр прямоугольника

"""

class rectangle():

    def __init__(self,len,width):
        self.l = len
        self.w = width

    def area(self):
        return self.l*self.w

    def perimetr(self):
        return 2*(self.l+self.w)

Test_rec_1 = rectangle(2,4)

print('Area:',Test_rec_1.area())
print('Perimetr:',Test_rec_1.perimetr())

Test_rec_2 = rectangle(1.2,8)
print('Area:',Test_rec_2.area())
print('Perimetr:',Test_rec_2.perimetr())