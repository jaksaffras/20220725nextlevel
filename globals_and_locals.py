"""
Hello. I am a doc string.
"""

color = "blue"


def spam():
    animal = "wombat"
    loc = locals()
    print(f"loc: {loc}")
    g = globals()
    print(f"g: {g}")

spam()

g = globals()

print(f"g['color']: {g['color']}")
print(f"color: {color}")

g['country'] = "Burkina Faso"
print(f"country: {country}")

g['bark'] = lambda : print("Woof! Woof!")

bark()








