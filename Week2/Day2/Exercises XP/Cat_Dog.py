#Exercise 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [Bengal('Razor',3), Chartreux('Peter',3), Siamese('Sima',4)]

sara_pets = Pets(all_cats)

for pet in sara_pets.animals:
    print(pet.walk())

#Exercise 2 : Dogs

class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking!'

    def run_speed(self):
        return round(self.weight/self.age*10,2)

    def fight(self, other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            print(f'The winner is {self.name}')
        else:
            print(f'The winner is {other_dog.name}')


dog1 = Dog('Rocket',5,34)
dog2 = Dog('Bob',7,23)
dog3 = Dog('Rox',2.5,12.5)

print(dog1.bark(),
dog2.bark(),
dog3.bark())

print(dog1.run_speed(), dog2.run_speed(), dog3.run_speed())


dog1.fight(dog2)
dog1.fight(dog3)
dog2.fight(dog3)

#Exercise 3 : Dogs Domesticated

