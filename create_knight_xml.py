import lxml.etree as et

root = et.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight = et.SubElement(root, 'knight', title=title)
        knight_name = et.SubElement(knight, 'name')
        knight_name.text = name
        et.SubElement(knight, 'color').text = color
        et.SubElement(knight, 'quest').text = quest

xml_doc = et.tostring(root, xml_declaration=True, pretty_print=True)
print(xml_doc.decode())
