from modules.library_item import LibraryItem
from modules.book import Book
from modules.cd import Cd
from modules.dvd import Dvd
from modules.magazine import Magazine
from modules.catalog import Catalog
import json


#item = LibraryItem('judul1', None, 'deskripsi judul 1')
#print(item.title)

#book = Book('isbn','authors', 'title', 'subject', 'dds_number', 'upc')
#print(book.title)

#cd = Cd('title CD', 'upc', 'subject', 'artist')
#print(cd.artist)

#dvd = Dvd('title Dvd', 'upc', 'subject', 'actors', 'director', 'genre')
#print(dvd.genre)

#magazine = Magazine('title Magazine', 'upc', 'subject', 'volume', 'issue')
#print(magazine.issue)

#input_search = 'test'
#result = Catalog(None).search('test')

f = open('files/data.json')
data_json = json.load(f)
#print(data_json)

list_book = []
list_magazine = []
list_dvd = []
list_cd = []

for item in data_json:
    if item['source']== 'book':
        list_book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            isbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source'] == 'magazine':
        list_magazine.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']
        ))

catalog_all = [list_book, list_magazine]

input_search = 'test'
result = Catalog(catalog_all).search(input_search)

print('====| results |====')
for index, result in enumerate(result):
    print(f'result ke-{index+1} | {result}')
#print(list_book)
#print("\n")
#print(list_magazine)
#print("\n")
#print("### print semua ###" + "\n")
#print(catalog_all)

