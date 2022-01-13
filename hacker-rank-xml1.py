import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    k=0
    for child in node.iter():
        l=child.attrib
        k += len(l)
    return k

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))