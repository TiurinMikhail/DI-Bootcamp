from Cat_Dog import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        Dog.__init__(self, name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self,*args):
        playing_dogs = [self.name]
        for dog in args:
            playing_dogs.append(dog.name)
        final_print = ', '.join(playing_dogs)
        print(final_print+' all play together')

    def do_a_trick(self):
        if self.trained:
            message = random.choice([f'{self.name} does a barrel roll', f'{self.name} stands on his back legs',
                       f'{self.name} shakes your hand', f'{self.name} plays dead'])
            print(message)

bully = PetDog("Bully",3,22)
lucky = PetDog("Lucky",10,30)
charley = PetDog("Charley",1.5,3)

bully.play(lucky,charley)

bully.train()
bully.do_a_trick()


#Exercise 4 : Family

class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self,**kwargs):
        print('Congratulations!')
        self.members.append(dict(kwargs, age=0, is_child=True))

    def is_18(self,name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    return True
                else:
                    return False
            else:
                print('There is no such member in family!')

    def family_presentation(self):
        print(f'The family {self.last_name}')
        for member in self.members:
            for key, value in sorted(member.items()):
                print(f'{key}:{value}')
            print('-------------------')
            #print(f'Name: {member["name"]}, age: {member["age"]}, gender: {member["gender"]}, is_child: {member["is_child"]}')


family1 = Family([
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ],'Goldman')

family1.family_presentation()
family1.born(name='Andrew', gender='Male')

family1.family_presentation()

print(family1.is_18('Sarah'))
print(family1.is_18('Andrew'))
print(family1.is_18('Michael'))

#Exercise 5 : TheIncredibles Family

class TheIncredibles(Family):
    def use_power(self, name):
        try:
            for member in self.members:
                if member['name'] == name and self.is_18(name):
                    print(f'{member["name"]} power is "{member["power"]}"')
                elif member['name'] == name and not self.is_18(name):
                    raise Exception(f'{name} is under 18!')
        except Exception as e:
            print(e)

    def incredible_presentation(self):
        print('*Here is our powerful family **\n',self.last_name)
        super().family_presentation()




family2 =  TheIncredibles([
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ],'Goldman')


family2.use_power('Michael')
print('-------------')
family2.incredible_presentation()
family2.born(name='Jack', gender='Male', power='Unknown power', incredible_name='Jack-Jack')
family2.incredible_presentation()
family2.use_power('Jack')







