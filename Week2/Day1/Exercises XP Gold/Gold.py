#Exercise 1 : Geometry
import math

pi = math.pi

class Circle:
    def __init__(self,circle_name,radius = 1):
        self.circle_name = circle_name
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * self.radius*pi
        return round(perimeter,2)
    def calculate_area(self):
        area = pi * self.radius**2
        return round(area,2)

    def definition(self):
        print("A circle is defined in geometry as the set of all points in a plane that are at a fixed distance from a given point, known as the center. This fixed distance is referred to as the radius of the circle. Essentially, a circle can be thought of as a closed curve that is perfectly round and smooth, with every point on the curve maintaining the same distance from the center point.")


circle1 = Circle("Circle1",4)
circle1.definition()
print(circle1.calculate_area())
print(circle1.calculate_perimeter())

#Exercise 2 : Custom List Class
import random

class MyList:
    def __init__(self,list_of_letters):
        self.list_of_letters = list_of_letters

    def reversed(self):
        return self.list_of_letters[::-1]

    def sorted(self):
        return sorted(self.list_of_letters)

    def generate_list(self):
        length = len(self.list_of_letters)
        return [random.randint(1,10) for num in range(length)]


my_list = MyList(["a",'b','c','d','t','u','y','x','k'])
print(my_list.sorted())
print(my_list.reversed())
print(my_list.generate_list())



