class Animal:
    alive = True        # живой
    fed = False         # накормленный
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = isinstance(food, Plant)
        if food.edible == True:
            Animal.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Plant:
    edible = False        # съедобный
    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    edible = True

class Flower(Plant):
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print()
print(a1.alive)
print(a2.fed)
print()
a1.eat(p1)
a2.eat(p2)
print()
print(a1.alive)
print(a2.fed)
