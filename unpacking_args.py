
def spam(x, y, z):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")

spam(5, 10, 15)

a = "man"
b = "bites"
c = "dog"

spam(a, b, c)

args = ['ham', 'toast', 'eggs']

# spam(args)

spam(*args)

def config(**values):
    print(f"values: {values}")

config(file_name="wombats.txt", country="Burkina Faso", color="chartreuse")


args = {
    'file_name': 'shrew_life.txt',
    'country': 'Tuvalu',
    'color': 'ecru'
}

config(**args)





