from pathlib import Path
import xml.etree.ElementTree as ET

my_dir = Path(__file__).parent
xml_file = my_dir / "groups.xml"

tree = ET.parse(xml_file)

root = tree.getroot()

for child in root:
    print(child.tag, child.attrib, child.text)
    for subchild in child:
        print(subchild.tag, subchild.attrib, subchild.text)
        for subsubchild in subchild:
            print(subsubchild.tag, subsubchild.attrib, subsubchild.text)

for chapter in root.findall("book/content/chapter"):
    print(chapter.tag, chapter.attrib, chapter.text)
for appendix in root.findall("book/content/appendix"):
    print(appendix.tag, appendix.attrib, appendix.text)


def write():
    # Створення кореневого елемента
    root = ET.Element('data')

    # Створення під-елементів та додавання їх до кореневого елемента
    child1 = ET.SubElement(root, 'child1')
    child1.text = 'Data 1'
    child2 = ET.SubElement(root, 'child2')
    child2.text = 'Data 2'

    # Запис у XML-файл
    tree = ET.ElementTree(root)
    tree.write('output.xml')

for item in root.findall("book/content"):
    appendix = item.find("appendix")
    if appendix is not None:
        a1 = appendix.find("a1")
        if a1 is not None:
            print(f"Item: {item.text}, appendix {appendix.text},  a1: {a1.text}")
