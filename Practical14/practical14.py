from xml.dom.minidom import parse 
import xml.dom.minidom
import pandas as pd
# Parse the 'go_obo.xml' file and obtain its root element.
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
# Extract all the term elements from the root element
terms = collection.getElementsByTagName('term')
Go_id, name, child_node, defstrs = [], [], [], []


# Define a function to find child nodes of a given GO ID
def find_is_a(go_id):
    child_nodes = []
    for term in terms:
        is_as = term.getElementsByTagName('is_a')
        for is_a in is_as:
            #  If the GO ID of the 'is_a' element matches the given GO ID, append the child node ID to 'child_nodes'
            if go_id == is_a.childNodes[0].data:
                child_nodes.append(term.getElementsByTagName('id')[0].childNodes[0].data)
                # Recursively call the function with the child node ID as input
                child_nodes += find_is_a(term.getElementsByTagName('id')[0].childNodes[0].data)
    return child_nodes


for i in terms:
    definition = i.getElementsByTagName('def')[0]
    defstr = definition.getElementsByTagName('defstr')[0]
    if 'autophagosome' in defstr.childNodes[0].data:
        # Append the GO ID, name, defstr, childnode to lists
        Go_id.append(i.getElementsByTagName('id')[0].childNodes[0].data)
        name.append(i.getElementsByTagName('name')[0].childNodes[0].data)
        defstrs.append(defstr.childNodes[0].data)
        child_node.append(len(find_is_a(i.getElementsByTagName('id')[0].childNodes[0].data)))
# Create a pandas DataFrame using the four lists, and save the DataFrame to an Excel file
df = pd.DataFrame({'id': Go_id, 'name': name, 'definition': defstrs, 'childnodes': child_node})
df.to_excel('autophagosome.xlsx', index=False)
