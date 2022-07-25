
customer_name = "Bob Smith"

x = 5    #  x = int(5)     JAVA:  int x = new int(5)     int x = 5;

print(x, x * 10)

y = x    #  y = <reference to> int(5) (sort of)

print(x, y)

print(x is y, id(x), id(y))


x = 50   #  x = int(5)  bound 'x' to new int object

print(x, y)

print(globals())

wombat = None
print(wombat)

#   a-z A-Z 0-9 _

#  customer_name   weekly_report

#  MAX_TRIES = 3

a: int = 123
b: str = "456"
# result = a + b
result = str(a) + b
print(f"result: {result}")
result = a + int(b)
print(f"result: {result}")

def spam(x: int) -> int:
    print(x * 3)

spam(b)


















