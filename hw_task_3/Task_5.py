"""
5.	* Доработайте задачу 4:
a.	при росте дерева у него случайным образом могут появиться новые плоды в первой стадии созревания.
b.	при сборе урожая собираются только спелые плоды.
c.	для деревьев добавьте параметр - возраст - параметр по умолчанию 1, при росте дерева параметр увеличивается на 1.
i.	На первых двух годах жизни дерево не имеет плодов.
ii.	Если возраст достиг 5 у дерева перестают появляться плоды.
iii.	Если возраст достиг 10 у дерева умирают все плоды.
d.	Для садовника добавьте метод который возвращает статистику по саду:
i.	кол-во деревьев, их возраст
ii.	кол-во яблок и их стадии.
e.	Если яблоко не собрано 3 цикла созревание оно умирает.

"""


class apple():
    grown_stage = ["blooming", 'green', 'red']
    index = 1

    def __init__(self):
        self.index = apple.index
        apple.index += 1
        self.stage = 0

    def ripe(self):
            self.stage += 1

    def is_ripe(self):
        if self.stage > 2:
            return True
        else:
            return False

    def ripe_stage(self):
        if 2 < self.stage < 5:
            return apple.grown_stage[2]
        elif self.stage >= 5:
            return False
        else:
            return apple.grown_stage[self.stage]

class tree():

    def __init__(self, num, *args):
        self.age = 1
        self.apples = []
        self.apples.extend(args)
        self.num = num

    def grow(self):
        import random
        self.age += 1
        if self.age >= 10:
            self.apples = []
        for ap in self.apples:
            ap.ripe()
            if ap.ripe_stage() == False:
                self.apples.remove(ap)
        if (2 < self.age < 5) and random.random() < 0.7:
            a = apple()
            self.apples.append(a)

    def num_apples_is_ripe(self):
        i = 0
        for apple in self.apples:
            if apple.is_ripe() == True:
                i += 1
        return i

    def grow_stage(self):
        ripe_dict = dict.fromkeys(['all','blooming', 'green', 'red'], 0)
        for apple in self.apples:
            ripe_dict[apple.ripe_stage()] += 1
            ripe_dict['all'] += 1
        return ripe_dict

    def harvest(self):
        i = 0
        for ap in self.apples:
            if ap.ripe_stage == 'red':
                self.apples.remove(ap)
                i +=1
        return (i)


class gardener():

    def __init__(self, name, *args):
        self.name = name
        self.trees = list(args)

    def water_the_plants(self):
        for plant in self.trees:
            plant.grow()

    def add_tree(self,tree):
        self.trees.append(tree)

    def harvest(self):
        for plant in self.trees:
            if plant.is_ripe():
                print(f'{plant.harvest()} apples harvested')
            else:
                print(f'Tree #{plant.num} is not ripe')

    def garden_stats(self):
        for tree in self.trees:
            print(f'Tree {self.trees.index(tree)} has age:{tree.age} and apples {tree.grow_stage()}')


tree_1 = tree(1)
tree_2 = tree(2)
Ivan = gardener('Ivan', tree_1,tree_2)
Ivan.garden_stats()

Ivan.water_the_plants()
Ivan.water_the_plants()
Ivan.garden_stats()



Ivan.water_the_plants()
Ivan.garden_stats()

Ivan.water_the_plants()
Ivan.garden_stats()

Ivan.water_the_plants()
Ivan.garden_stats()

Ivan.water_the_plants()
Ivan.garden_stats()

Ivan.water_the_plants()
Ivan.garden_stats()

Ivan.water_the_plants()
Ivan.garden_stats()

Ivan.water_the_plants()
Ivan.garden_stats()

# print(tree.ripe_stage())
# gardener.water_the_plants()
# print(tree.ripe_stage())
# gardener.harvest()
# gardener.water_the_plants()
# print(tree.ripe_stage())
# gardener.harvest()
# gardener.water_the_plants()

