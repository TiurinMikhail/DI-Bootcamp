class Farm:
    def __init__(self,farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self,animal,number = 1):
        if animal not in self.animals.keys():
            self.animals[animal] = number
        else:
            self.animals[animal] += number

    def get_info(self):
        print(f"{self.farm_name}'s farm\n")
        for animal,number in self.animals.items():
            print(f"{animal} : {number}")
        print()
        print('    E - I - E - I - O!')


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 2)
macdonald.get_info()