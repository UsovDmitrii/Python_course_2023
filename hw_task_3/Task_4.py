"""
4.	Создайте классовую структуру по описанию
a.	Имеется яблоко со следующими характеристиками:
i.	индекс - принимается при инициализации
ii.	Стадии созревания (цветение, зеленое, красное) - список хранится в классе, как константа
iii.	Стадия созревания - создается при инициализации, по умолчанию первое значение из списка стадий
b.	Яблоко может:
i.	созревать (переходить на следующую стадию созревания)
ii.	предоставлять информацию о своей зрелости - если яблоко созрело метод возвращает True иначе False
c.	Имеется дерево с яблоками:
i.	дерево содержит список яблок которые на нем растут - яблоки принимаются при инициализации, как неизвестное кол-во параметров. Сохраняются в список
d.	Дерево может:
i.	расти вместе с яблоками - т.е. каждое яблоко должно созреть на 1 стадию.
ii.	предоставлять информацию о зрелости всех яблок - если все яблоки созрели возвращать True иначе False.
iii.	предоставлять урожай - удалять все яблоки.
e.	Имеется садовник, который имеет:
i.	имя - принимается  при инициализации.
ii.	растения, за которыми следит - принимаются при инициализации, как неизвестное кол-во параметров. Сохраняются в список
f.	Садовник может:
i.	ухаживать за растениями - для каждого растения вызывать метод роста.
ii.	собирать урожай - удалять все яблоки - только в том случае если все яблоки созрели. Иначе выдавать предупреждение.


		Для тестирования:
-	создайте 5 яблок, 1 дерево и 1 садовника
-	используя садовника поухаживайте за деревьями
-	Соберите урожай когда все яблоки созреют.
"""

class apple():
    grown_stage = ["blooming",'green','red']

    def __init__(self,index):
        self.index=index
        self.stage = 0

    def ripe(self):
        if self.stage < 2:
            self.stage += 1
    def is_ripe(self):
        if self.stage == 2:
            return True
        else:
            return False

    def ripe_stage(self):
        return apple.grown_stage[self.stage]

class tree():

    def __init__(self,num,*args):
        self.apples = []
        self.apples.extend(args)
        self.num = num

    def ripe(self):
        for apple in self.apples:
            apple.ripe()

    def is_ripe(self):
        i = True
        for apple in self.apples:
            if apple.is_ripe() == False:
                i = False
        return i

    def ripe_stage(self):
        ripe_dict = dict.fromkeys(["blooming",'green','red'],0)
        for apple in self.apples:
            ripe_dict[apple.ripe_stage()] += 1
        return ripe_dict

    def harvest(self):
        i = len(self.apples)
        self.apples = []
        return (i)

class gardener():

    def __init__(self,name,*args):
        self.name = name
        self.trees = args

    def water_the_plants(self):
        for plant in self.trees:
            plant.ripe()

    def harvest(self):
        for plant in self.trees:
            if plant.is_ripe():
                print(f'{plant.harvest()} apples harvested')
            else:
                print(f'Tree #{plant.num} is not ripe')

apple_1 = apple(1)
apple_2 = apple(2)
apple_3 = apple(3)
apple_4 = apple(4)
apple_5 = apple(5)

tree = tree(1,apple_1,apple_2,apple_3,apple_4,apple_5)
gardener = gardener('Ivan',tree)

print(tree.ripe_stage())
gardener.water_the_plants()
print(tree.ripe_stage())
gardener.harvest()
gardener.water_the_plants()
print(tree.ripe_stage())
gardener.harvest()
gardener.water_the_plants()

gardener.water_the_plants()
gardener.harvest()
