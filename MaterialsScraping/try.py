import requests, os, bs4
import selectors
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://heatexchanger-fouling.com/proceedings19.htm')
bs = BeautifulSoup(html, 'html.parser')

links_all = bs.find_all('a', href=True)

links2019 = links_all[12:57]
print(links2019[0])

type(links2019[0])

#a href="papers/papers2019/01_Jibbs et al.pdf"><b>HELIXCHANGER® Heat Exchanger - Field Experience and Ongoing Development</b><br/>R.J. Jibb, M. Brignone, S. Taha, G. Podrebarac, J. Larance, P. Junge </a>
