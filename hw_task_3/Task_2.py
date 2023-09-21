"""
2.	Напишите программу - виртуальную модель процесса обучения.
В программе должны быть объекты: ученик, учитель, учебные материалы.
У каждого учителя должны быть атрибут:
-	количество обученных учеников
		Для учителя добавьте метод “teach”:
-	Метод принимает строку “название материала” и неизвестное количество учеников.
-	Для каждого ученика вызывается метод “take” из класса ученика с параметром “название материала”.
-	Атрибут учителя “количество обученных учеников” увеличивается на 1.
		У каждого ученика должен быть атрибут “knowledge” - список знаний.
		Для ученика создайте метод “take”
-	метод принимает строку знаний и добавляет ее в список знаний ученика.
		Класс учебных материалов
-	должен принимать любое количество не именованных атрибутов и при инициализации сохранять в один атрибут в виде списка.

"""


class teacher():

    def __init__(self):
        self.trained_students = 0

    def teach(self, title=str, *args):
        for student in args:
            student.take(title)
            self.trained_students += 1


class student():

    def __init__(self):
        self.knowledge = []

    def take(self, title=str):
        self.knowledge.append(title)



class educational_material():

    def __init__(self, *args):
        self.materials = []
        for m in args:
            self.materials.append(m)

it_material=educational_material("Python","Version Control Systems","Relational Databases","NoSQL databases","Message Brokers")
main_teacher= teacher()

student_sam = student()
student_frodo = student()
student_mary = student()
student_pipin = student()

main_teacher.teach("Python",student_sam,student_frodo)
main_teacher.teach("Relational Databases",student_pipin,student_frodo)
main_teacher.teach("NoSQL databases",student_sam,student_mary)
main_teacher.teach("Message Brokers",student_pipin,student_mary)
main_teacher.teach("Version Control Systems",student_sam,student_frodo)

print("student_sam", student_sam.knowledge)
print("student_frodo", student_frodo.knowledge)
print("student_mary", student_mary.knowledge)
print("student_pipin", student_pipin.knowledge)

print(main_teacher.trained_students)

