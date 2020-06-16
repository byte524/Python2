import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import datetime

class Parser():
    def __init__(self, site):
        self.site = site
    def Pars(self):
        u = urllib.request.urlopen(self.site).read()
        sp = BeautifulSoup(u,'lxml')
        pr = sp.body
        pr = pr.select("tr:nth-of-type(1) > td:nth-of-type(4)")
        return str(pr).replace("[<td>","").replace("</td>]","")

print('Для выхода нажмите "CTRL+C"')
while True:
    url = Parser("https://www.banki.ru/products/currency/cb/")
    now = datetime.datetime.now()
    a = now.strftime("%d-%m-%Y %H:%M")

    with open('1.txt','a') as o:
        o.write(str(a)+' '+ str(url.Pars())+'\n')
    sleep(3600)
