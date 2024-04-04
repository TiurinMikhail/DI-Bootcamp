class Dog:
    def __init__(self, name, color, age=0):
        print('Dog has been created')
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        print(f'{self.name} goes Wof!!')

    def upper(self):
            print(self.name.upper())

    def walk(self, meters):
        print(f'{self.name} walked {meters} meters')

    def rename(self, new_name):
        self.name = new_name


# creating objects:

shelter_dog = Dog("Rex", "brown")
pitbull_dog = Dog("Fera", "grey")
chowchow = Dog("Nika", "orange")


chowchow.favotite_toy = 'ball'

print(pitbull_dog.name,pitbull_dog.age,pitbull_dog.color)
print(shelter_dog.name,shelter_dog.age,shelter_dog.color)

print(chowchow.favotite_toy)

#calling methods in the object
chowchow.bark()
chowchow.upper()
chowchow.walk(500)
shelter_dog.walk(100)
pitbull_dog.walk(150)

pitbull_dog.rename('Fluffy')
print(pitbull_dog.name)



class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)



class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

  def modify_name(self,surname):
    self.surname = surname


first_person = Person("John", 36)
first_person.show_details()

first_person.modify_name('Jackson')
print(first_person.surname)
first_person.modify_name('Madison')
print(first_person.surname)

print(first_person.__dict__)



class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")

xiaomi_computer = Computer()
Computer.description(xiaomi_computer, "Redmi")

print(max(pitbull_dog.age,chowchow.age))