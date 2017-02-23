import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

import bs4 as bs

import urllib.request

import pandas as pd

#basics
'''
source = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

print(soup.title.text)

print(soup.p)

print(soup.find_all('p>'))

for paragraph in soup.find_all('p'):
    print(paragraph.text)

print(soup.get_text())
[print(url.get('href')) for url in soup.find_all('a')]
'''

#navigation
'''
nav = soup.nav
[print(url.get('href')) for url in nav.find_all('a')]

[print(div.text) for div in soup.find_all('div', class_='body')]
'''

#tables and xml
'''
table = soup.table #soup.find('table')

table_rows = table.find_all('tr')

[print([i.text for i in tr.find_all('td')]) for tr in table_rows] #rows
'''

##pandas
'''
dfs = pd.read_html('http://pythonprogramming.net/parsememcparseface/', header=0)

[print(df) for df in dfs]
'''

##XML
'''
source = urllib.request.urlopen('http://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source, 'xml')

f = open('mapa_adres', 'w')
[f.write(url.text + '\n') for url in soup.find_all('loc')]
f.close()
'''

#Dynamic javascript scraping

class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

url = 'http://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()

#source = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/')

soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)




