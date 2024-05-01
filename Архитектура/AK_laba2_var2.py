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


while True:
    print()
    print("1.Вывод")
    print("2.Добавить ")
    print("3.Удалить")
    vvod = input("Введите число ")
    if (vvod == "1"):
        findobj = input("Введите тег дл поиска ")
        for find in root.iter(findobj):
            for child in find:
                print(child.tag, child.text)

    elif(vvod == "2"):
        vvod_playse = input("Введите тег, куда добавить ")
        vvod_new_teg = input("Введите имя нового тега ")
        vvod_text_new_teg = input("Введите текст тега ")
        playse = root.find(vvod_playse)
        el = et.Element(vvod_new_teg)
        playse.append(el)
        el.text = vvod_text_new_teg
        tree.write('AK_laba2.xml')

    elif(vvod == "3"):
        vvod_gl_teg = root.find(input("Введите тегиз которого удалять "))
        vvod_del_teg = vvod_gl_teg.find(input("Введите тег для удаления "))
        vvod_gl_teg.remove(vvod_del_teg)
        tree.write('AK_laba2.xml')


note1.remove(elem)
