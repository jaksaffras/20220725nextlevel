import math

def junk():
    pass

x = junk()

print(f"x: {x}")


def get_message():
    return "Hello, world"

message = get_message()
print(f"message: {message}")

def rectangle_area(length, width):
    return length * width

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

a = rectangle_area(5, 10)
print(f"a: {a}")

print(f"circle_area(22): {circle_area(22)}")

def wacky(pos1, pos2, *args, name1, name2, **kwargs):
    print(f"pos1: {pos1}")
    print(f"pos2: {pos2}")
    print(f"args: {args}")
    print(f"name1: {name1}")
    print(f"name2: {name2}")
    print(f"kwargs: {kwargs}")
    print()

wacky(10, 20, name1=30, name2=40)

wacky(10, 20, 30, 40, 50, name1=100, name2=200, wombat=300, toast=72)



def get_lines_matching_string(str_to_match, *file_paths, ignore_case=False):
    matching_lines = []
    if ignore_case:
        str_to_match = str_to_match.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                original_line = line
                if ignore_case:
                    line = line.lower()
                if str_to_match in line:
                    matching_lines.append(original_line.rstrip())

    return matching_lines

results = get_lines_matching_string("lizard", 'DATA/words.txt', 'DATA/alice.txt')
print(results)

results = get_lines_matching_string("lizard", 'DATA/words.txt', 'DATA/alice.txt', ignore_case=True)
print(results)
















