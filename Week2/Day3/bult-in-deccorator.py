# Built-in Decorators:

#staticmethod
#class MyClass:
  #@staticmethod
  #def add(a, b):
    #return a + b

#print(MyClass.add(3, 6))
# >> 9

#classmethod

class MyClass:
  counter = 0

  @classmethod
  def add(cls,a):
    cls.counter += 1
    return cls.counter


MyClass.add(3)
print(MyClass.counter)

my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))
# >> 3


class Circle:
    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter

    @classmethod
    def from_radius(cls,radius):
        return cls(radius = radius , diameter = radius*2)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter/2, diameter=diameter)

corcle_obj = Circle.from_radius(5)
print(corcle_obj.diameter)
circle_obj = Circle.from_diameter(12)
print(circle_obj.radius)