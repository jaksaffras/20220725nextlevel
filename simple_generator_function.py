

def spam():
    for x in 10, 20, 30, 40:
        yield x


s = spam()
print(f"s: {s}")
for value in s:
    print(value)
print()
