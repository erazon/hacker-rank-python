import xml.etree.ElementTree as etree


def get_attr_number(node):
    return sum([len(element.items()) for element in node.iter()])


if __name__ == '__main__':
    xml = ""
    for _ in range(int(input())):
        xml += input()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
