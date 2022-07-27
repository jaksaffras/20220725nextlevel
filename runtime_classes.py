
#            name      super attrs
Animal = type("Animal", (), {})

print(f"Animal: {Animal}")
a = Animal()
print(f"a: {a}")


Dog = type('Dog', (Animal,), {'bark': lambda self: print("woof woof")})

d1 = Dog()
d2 = Dog()

for dog in (d1, d2):
    dog.bark()


for s in 'spam', 'ham':
    print(s.upper())


