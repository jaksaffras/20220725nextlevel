x = "submarine"

actor = "Chris Hemsworth"   # global scope (file scope)

def spam():
    x = 100  # local scope
    print("in spam(): x is", x)
    print("in spam(): actor is", actor)

spam()

# def len(obj):
#     return "HA HA HA"

print(len(actor))


print(f"in main: x: {x}")   # x is not in scope

#  local -> nonglobal -> global -> builtin


def fram(color):
    x = 1000

    def blam():
        print("in blam(): color is", color)
        print("in blam(): x is", x)

    return blam










