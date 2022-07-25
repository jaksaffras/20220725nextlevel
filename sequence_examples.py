fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

actor = "Chris Hemsworth"
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(fruits[0], actor[0], person[0])
print(fruits[-1], actor[-1], person[len(person)-1], '\n')

#   [start:sentinel]
#   [start:stop]   [:stop]   [start:]  [start:stop:step]
print(f"fruits[0:4]: {fruits[0:4]}")

print(f"fruits[7:12]: {fruits[7:12]}")
print(f"actor[:5]: {actor[:5]}")
print(f"actor[6:9]: {actor[6:9]}")

print(f"person[:2]: {person[:2]}")
print(f"actor[-9:]: {actor[-9:]}")
print(f"fruits[-5:]: {fruits[-5:]}")
print(f"fruits[1:]: {fruits[1:]}")

# for file_path in sys.argv[1:]:   skip the script name (sys.argv[0])
#     ...
#     ...

# print(attr for attr in dir(fruits) if not attr.startswith('_') )



