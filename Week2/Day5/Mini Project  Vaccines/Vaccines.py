
class Human:
    blood_types = ['A', 'B', 'AB', 'O']

    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = int(age)
        self.priority = priority
        while True:
            if blood_type.upper() not in self.blood_types:
                raise ValueError('You must enter a valid blood type')
            else:
                self.blood_type = blood_type
                break
        self.family = []

    def __str__(self):
        return f'id:{self.id_number}, name:{self.name}, age:{self.age}, priority:{self.priority}, blood type:{self.blood_type}'

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)

class Queue:
    def __init__(self):
        self.humans = []

    def __str__(self):
        stroke = ''
        for human in self.humans:
            stroke += str(human) + '\n'
        return stroke

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for index, human in enumerate(self.humans):
            if human.id_number == person.id_number:
                return index
        return None

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 is not None and index2 is not None:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if self.humans:
            return self.humans.pop(0)
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for i, human in enumerate(self.humans):
            if human.blood_type == blood_type:
                return self.humans.pop(i)
        return None

    def sort_by_age(self):
        self.humans = sorted(self.humans, key=lambda human: (human.priority, human.age),reverse=True)
        return self

    def rearrange_queue(self):
        new_queue = []
        for i, human in enumerate(self.humans):
            if i != len(self.humans) -1 and self.humans[i] in self.humans[i+1].family:
                self.humans.append(self.humans.pop(i))

        # new_queue = []
        # i = 0
        # while i < len(self.humans):
        #     new_queue.append(self.humans[i])
        #     if i < len(self.humans) - 1 and any(
        #             member in self.humans[i].family for member in self.humans[i + 1].family):
        #         new_queue.append(self.humans.pop(i + 1))
        #     else:
        #         i += 1
        # self.humans = new_queue

human1 = Human(1, 'Antonio', 20, False, 'A')
human2 = Human(12, 'Marco', 24, False, 'B')
human3 = Human(3, 'Marconi', 64, False, 'AB')
human4 = Human(4, 'Mubarak',55,True,'O')
human5 = Human(5, 'Morris',63,True,'B')
human6 = Human(2, 'Andrew',28,False,'B')
human7 = Human(7, 'Tony',29,True,'AB')

queue1 = Queue()

queue1.add_person(human1)
queue1.add_person(human2)
queue1.add_person(human3)
queue1.add_person(human4)
queue1.add_person(human5)
queue1.add_person(human6)
queue1.add_person(human7)

print(queue1)
print(queue1.sort_by_age())
print()

human2.add_family_member(human6)
queue1.rearrange_queue()
print(queue1)

