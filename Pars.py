#Імпортую всі потріні бібліотеки
import requests
from bs4 import BeautifulSoup
import numpy as np
import re
url = requests.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2')
wiki_text = url.text
soup = BeautifulSoup(wiki_text, 'lxml')

#Пошук за допомогою bs4 всіх тегів tr
country = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('td')
# Пошук першої назви країни
name = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('td')[2].text
# пошук першої повної назви країни
fullname = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('td')[3].text
# Пошук довжини першої повної назви країни
length = len(fullname)
#Пошук першого посилання
flags = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('a')[0].get('href')
#Пошук всіх посилань на сторінці
flag = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('a')

#Створив всі пусті масиви які використаю
data = []
names = []
fullnames = []
lengths = []
Flag = []
count_same = []
low = []
up = []
rens = []

# Створив список з усіх назв країн
for i in range (2, len(country), 4):
    name = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('td')[i].text
    names.append(name.strip())
# Створив список з усіх повних назв країн
for k in range(2, len(country), 4):
    fullname = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('td')[k+1].text
    fullnames.append(fullname.strip())
# Створив список з усіх довжин повних назв країн
for p in range(2, len(country), 4):
    length = len((soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('td')[p+1].text).replace(' ', ''))-1
    lengths.append(length)
# Створив список з усіх посиань на прапор країн
for j in range(0, len(flag), 2):
    flags = soup.find('div', class_='mw-parser-output').find('table', class_='wikitable').find('tbody').find_all('a')[j].get('href')
    Flag.append(flags)

# Створив список щоб всі назви країн починались на малу літеру
for lows in names:
    low.append(lows.lower())

# Створив список що у країн з подвійною назвою велика буква була тільки у першого слова
# щоб метод re.findall не враховував велику літеру
# Приклад було (Антигуа и Барбуда) стало (Антигуа и барбуда)
for r in range(0, len(low)):
    up.append(low[r][0].upper())
#Створив список країн які починаються на ту ж літеру
for n in range(0, len(up)):
    ren = re.findall(up[n][0], str(up))
    rens.append(len(ren))

# Ствоив фінальний список де виведу всі потрібні атрибути
for t in range(0, len(names)):
    data.append({
        'Country': names[t],
        'Country_full_name' : fullnames[t],
        'Length_word': lengths[t],
        'Flag_url': Flag[t],
        'Same_letter_count': rens[t]
    })
print(np.array(data))
print()
# Функція що виводить дані за назвою країни
def para(name_country):
   ind = names.index(name_country)
   print(data[ind])

para('Австрия')