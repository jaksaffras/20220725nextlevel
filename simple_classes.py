
cities = list()   #  list cities = new list()

cities.append("Newark")
cities.append("Albany")
cities.append("Austin")
print(f"cities: {cities}")

print(f"type(cities): {type(cities)}")

fruits = list()
cheeses = list()

class Animal:
    def spam(self):
        print("SPAM!")

generic_animal = Animal()

print(Animal, generic_animal, type(generic_animal))

class Dog(Animal):
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d2 = Dog()
d3 = Dog()
d1.bark()
d2.bark()
d3.bark()
d2.spam()


