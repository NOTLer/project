import xml.etree.ElementTree as et

tree = et.parse("AK_laba2.xml")
root = tree.getroot()

print(root)
print(root.tag, root.attrib)


def probj(obj):
    for child in obj:
        print(child.tag, child.attrib)
        for child1 in child:
            print(child1.tag, child1.text)


def delobj(obj, delob):
    obj.remove(delob)


def addobj(obj, addob):
    obj.append(addob)


note1 = root[0]
elem = et.Element('condition')
note1.append(elem)
elem.text = 'new'
probj(root)

note1.remove(elem)
tree.write('AK_laba2.xml')
