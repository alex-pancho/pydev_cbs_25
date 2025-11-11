import xml.etree.ElementTree as ET
from pathlib import Path


xml_file_path = Path(__file__).parent / "xml.xml"

# Завантаження XML-файлу
tree = ET.parse(xml_file_path)
root = tree.getroot()

for child in root:
    print(child.tag, child.text, child.attrib)
    for subchild in child:
        print(">>", subchild.tag, subchild.text, subchild.attrib)

for content in root.findall("book/content"):
    print("&&&", content.tag, content.text, content.attrib)
    chapters = content.findall("chapter")  
    for chapter in chapters:
        print("&&&", chapter.tag, chapter.text, chapter.attrib)
    
    appendix = content.find("appendix")
    if appendix is not None:
        print("<<", appendix.tag, appendix.attrib, appendix.text)


appendix = root.find('.//appendix')

# Виводимо текст
if appendix is not None:
    print(appendix.text.strip(), appendix.attrib)
else:
    print("Елемент <appendix> не знайдено.")