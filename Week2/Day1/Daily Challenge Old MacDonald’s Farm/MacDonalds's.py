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

    def get_animal_types(self):
        sorted_animals = sorted([key for key in self.animals.keys()])
        return sorted_animals

    def get_short_info(self):
        sorted_animals = self.get_animal_types()
        final_print = f"{self.farm_name}'s farm has "
        for index,animal in enumerate(sorted_animals):
            if self.animals[animal] <= 1 and index == len(sorted_animals) - 2:
                final_print += f'{animal}'
            elif self.animals[animal] > 1 and index == len(sorted_animals) - 2:
                final_print += f'{animal}s '
            elif self.animals[animal] > 1 and index != len(sorted_animals) - 1:
                final_print += f'{animal}s, '
            elif self.animals[animal] > 1 and index == len(sorted_animals) - 1:
                final_print += f'and {animal}s.'
            elif self.animals[animal] <= 1 and index == len(sorted_animals) - 1:
                final_print += f'and {animal}.'
            elif self.animals[animal] <= 1 and index != len(sorted_animals) - 1:
                final_print += f'{animal},'
        return final_print


macdonald = Farm("McDonald")

macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 2)

macdonald.get_info()

print(macdonald.get_animal_types())

print(macdonald.get_short_info())