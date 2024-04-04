class Door:
    def __init__(self, is_opened=True):
        self.is_opened = is_opened

    def open_door(self):
        if self.is_opened:
            print("Door already opened")
        else:
            self.is_opened = True
            print("Door is opened!")

    def close_door(self):
        if not self.is_opened:
            print("Door already closed")
        else:
            self.is_opened = False
            print("Door is closed!")


class BlockedDoor(Door):
    def __init__(self, is_opened=False):
        super().__init__(is_opened)

    def open_door(self):
        print("Door is blocked! You can not open a Blocked door!")

    def close_door(self):
        print("Door is blocked! You can not close a Blocked door!")


door1 = Door(True)
door1.open_door()
door1.close_door()
door1.open_door()
print()
block_door = BlockedDoor()
block_door.open_door()
block_door.close_door()


class Alien():
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def fly(self):
        print(self.name, 'is flying!')

    def sleep(self):
        print("Aliens don't sleep")

class Animal():
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("zzzZZZZZ")

class Dog(Animal):
    def bark(self):
        print("{} barked, WAF !".format(self.name))

class AlienDog(Dog,Alien):
    def __init__(self, name, planet):
        super().__init__(name)
        Alien.__init__(self, name, planet)


alien_dog = AlienDog("Rex",'Jypiter')
print(alien_dog.name, alien_dog.planet)
alien_dog.sleep()