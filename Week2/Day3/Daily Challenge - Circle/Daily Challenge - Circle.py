import math

class Circle:

    def __init__(self,radius, diameter):
        self.radius = radius
        self.diameter = diameter

    @classmethod
    def from_radius(cls, radius):
        return cls(radius=radius, diameter=radius * 2)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius= diameter / 2, diameter=diameter)

    def get_area(self):
        area = round(self.radius**2 * math.pi,3)
        return f'The area of circle is {area}'

    def __str__(self):
        return f'Circle with radius {self.radius} and diameter {self.diameter}.'

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle.from_radius(self.radius + other.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return Circle.from_radius(self.radius + other)

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius

    @classmethod
    def sort_circle(cls, circles_list):
        sorted_circles = sorted(circles_list, key=lambda circle: circle.radius)
        print('Sorted circle list: ')
        for item in sorted_circles:
            print(item)
        return sorted_circles



#A Circle can be defined by either specifying the radius or the diameter.
#The user can query the circle for either its radius or diameter.
circle1 = Circle.from_radius(16)
circle2 = Circle(radius=8, diameter=16)
circle3 = circle1.from_diameter(64)

print(circle1)
print(circle2)
print(circle3)

#Compute the circle’s area
#circle1_area = circle1.get_area()
#print(circle1_area)
print(circle1.get_area())

#Be able to add two circles together, and return a new circle with the new radius - use a dunder method
c4 = circle1 + circle2
print(c4)

print('-----')
#Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
print(circle1 < circle2)
print(circle1 > circle2)
print(circle1 >= circle3)
print(circle1 <= circle3)
print('-----')
#Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
print(circle1 == circle3)

print('-----')
#Be able to put them in a list and sort them
Circle.sort_circle([circle1, circle2, circle3])

#Bonus
import turtle

tur = turtle.Turtle()

for i, circle in enumerate(Circle.sort_circle([circle1, circle2, circle3])):
    tur.circle(circle.radius)

turtle.mainloop()



