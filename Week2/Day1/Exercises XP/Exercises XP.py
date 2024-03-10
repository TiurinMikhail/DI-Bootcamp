#Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

meinkun = Cat("Gordon",7)
ru_blue = Cat('Pie',9)
sphinx = Cat('Rocket',5)


my_cats = [meinkun, ru_blue, sphinx]

def oldest(list_of_cats):
    max_age = 0
    for cat in list_of_cats:
        if cat.age > max_age:
            max_age = cat.age
            max_age_cat = cat.name

    return max_age_cat, max_age

oldest_cat,max_age = oldest(my_cats)

print(f'The oldest cat is {oldest_cat}, and is {max_age} years old.')

#Exercise 2 : Dogs
class Dog:
    def __init__(self, name, height):
        print('Dog has been created')
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes Wof!!')

    def jump(self):
        x = self.height*2
        print(f'{self.name} jumps {x} cm high!')

davids_dog = Dog("Rex",50)

print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup",20)

print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog.name} is bigger than {davids_dog.name}')
elif sarahs_dog.height < davids_dog.height:
    print(f'{davids_dog.name} is bigger than {sarahs_dog.name}')
else:
    print('They have the same height')
######
print()
#Exercise 3 : Who’s The Song Producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


#Exercise 4 : Afternoon At The Zoo

class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        dictionary_alphabet = {}
        self.animals.sort()
        for animal in self.animals:
            if animal[0] not in dictionary_alphabet.keys():
                dictionary_alphabet[animal[0]] = [animal]
            else:
                dictionary_alphabet[animal[0]].append(animal)
        return dictionary_alphabet
    def get_groups(self):
        dictionary_alphabet = {}
        self.animals.sort()
        for animal in self.animals:
            if animal[0] not in dictionary_alphabet.keys():
                dictionary_alphabet[animal[0]] = [animal]
            else:
                dictionary_alphabet[animal[0]].append(animal)
        for index,group in enumerate(dictionary_alphabet.values()):
            if len(group) > 1:
                print(f'{index+1}:{group}')
            else:
                print(f'{index+1}:"{group[0]}"')

tel_aviv_zoo = Zoo("tel_aviv_zoo")
tel_aviv_zoo.add_animal("Ape")
tel_aviv_zoo.add_animal("Baboon")
tel_aviv_zoo.add_animal("Bear")
print(tel_aviv_zoo.animals)
print()
tel_aviv_zoo.sort_animals()
tel_aviv_zoo.get_groups()

ramat_gan_safari = Zoo("ramat_gan_safari")
ramat_gan_safari.add_animal('Tiger')
ramat_gan_safari.add_animal('Elefant')
ramat_gan_safari.add_animal('Leopard')
ramat_gan_safari.sell_animal('Tiger')
ramat_gan_safari.get_groups()
ramat_gan_safari.get_animals()

sorted_animals = ramat_gan_safari.sort_animals()
print(sorted_animals)