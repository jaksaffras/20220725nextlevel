

celsius = "40\u00B0"  # \uXXXX (FFFF) \UXXXXXXXX
print(f"celsius: {celsius}")

# utf-8
print(f"len(celsius): {len(celsius)}")

bcelsius = celsius.encode() # bytes

print(f"bcelsius: {bcelsius}")
print(f"len(bcelsius): {len(bcelsius)}")

print(f"bcelsius[0]: {bcelsius[0]}")

for b in bcelsius:
    print(b, hex(b))

c2 = bcelsius.decode()
print(f"c2: {c2}")

