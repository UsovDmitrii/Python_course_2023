"""
3.	доработайте задачу 2
a.	Классы “ученик” и “учитель” должны быть наследованы от класса “человек”.
i.	У каждого человека должны быть атрибуты: ФИО, возраст, пол.
b.	Для классов “Материалы” и “Ученик” добавьте магический метод, для вызова функции len() от объектов классов.
Материалы должны возвращать кол-во материалов, ученики кол-во знаний.
c.	добавьте в класс ученика, метод, позволяющий ученику случайно "забывать" какую-нибудь часть своих знаний.

"""


class person():

    def __init__(self, person_staff):
        print(person_staff.keys())
        self.name = None
        self.age = None
        self.sex = None

        if 'name' in person_staff.keys():
            self.name = person_staff['name']
        if 'age' in person_staff.keys():
            self.age = person_staff['age']
        if 'sex' in person_staff.keys():
            self.sex = person_staff['sex']

    def introducing(self):
        print(f'My name is {self.name}, I am {self.sex}, {self.age} years old')


class teacher(person):

    def __init__(self, **kwargs):
        self.trained_students = 0
        print(kwargs)
        if kwargs != None:
            super().__init__(kwargs)

    def teach(self, title=str, *args):
        for student in args:
            student.take(title)
            self.trained_students += 1


class student(person):

    def __init__(self, **kwargs):
        self.knowledge = []
        if kwargs != None:
            super().__init__(kwargs)

    def __len__(self):
        return len(self.knowledge)

    def take(self, title=str):
        self.knowledge.append(title)

    def forget(self):
        import random
        i = random.randint(0,len(self))
        self.knowledge.pop(i)


class educational_material():

    def __init__(self, *args):
        self.materials = []
        for m in args:
            self.materials.append(m)

    def __len__(self):
        return len(self.materials)


it_material = educational_material("Python", "Version Control Systems", "Relational Databases", "NoSQL databases",
                                   "Message Brokers")
main_teacher = teacher(name='Gandalf', age=120, sex='male')

student_sam = student(name='Sam',age = 40)
student_frodo = student(name='Frodo',age = 36)
student_mary = student(name='Mary',age = 32)
student_pipin = student(name='Pipin',age = 33)

main_teacher.introducing()

main_teacher.teach("Python", student_sam, student_frodo)
main_teacher.teach("Relational Databases", student_pipin, student_frodo)
main_teacher.teach("NoSQL databases", student_sam, student_mary)
main_teacher.teach("Message Brokers", student_pipin, student_mary)
main_teacher.teach("Version Control Systems", student_sam, student_frodo)


print("student_frodo", student_frodo.knowledge)
print("student_mary", student_mary.knowledge)
print("student_pipin", student_pipin.knowledge)
print(f"Student sam knowledge before exam was {len(student_sam)} unit: {student_sam.knowledge}" )
student_sam.forget()
print(f"Student sam knowledge after exam became {len(student_sam)} unit: {student_sam.knowledge}" )

