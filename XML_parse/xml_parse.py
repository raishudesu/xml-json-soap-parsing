import xml.etree.ElementTree as ET

#create tree and root objects
tree = ET.parse('books.xml')
root = tree.getroot()

print("\n-----#printing the id of books using .attrib-----")
#printing the id of books using .attrib
for book in root:
    print(book.attrib)

print("\n-----#finding book details in the xml file-----")
#finding books in the xml file
for book in root.findall('book'):
    author = book.find('author').text
    title = book.find('title').text
    price = book.find('price').text
    print(author, title, price)

print('\n-----#another way to do specified loop thru the file using iter()-----')
#another way to find details of the file using iter()
for book in root.iter('title'):
    print(book.text)