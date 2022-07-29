import lxml.etree as et

doc = et.parse('DATA/solar.xml')

print(f"doc: {doc}")

root = doc.getroot()
print(f"root: {root}")
print(f"root.tag: {root.tag}")

for section in root:
    if section.tag.endswith('planets'):
        for planet in section.findall('planet'):
            print(planet.get("planetname"))
            for moon in planet.findall('moon'):
                print(f"   {moon.text}")

