from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


html = urlopen('http://heatexchanger-fouling.com/proceedings19.htm')
bs = BeautifulSoup(html, 'html.parser')

links_all = bs.find_all('a', href=True)

links2019 = links_all[12:57]
link0 = links2019[0]

for tag in links2019:
    print(tag['href'])


#print(len(links2019), link0)

#paper0 = requests.get(link0)
#paper0.raise_for_status()

