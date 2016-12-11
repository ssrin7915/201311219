import urllib
from urlparse import urljoin
from lxml import etree
import codecs

f=codecs.open('nhcardBenefit.txt','w','utf-8')

tree=etree.HTML(urllib.urlopen('https://card.nonghyup.com/servlet/IPCC2011I.view').read())
cardList= tree.xpath('//*[@id="resultHTML"]')
for card in cardList[0].xpath('ul/li'):
    title=card.xpath('strong/span/text()')[0]
    detail= card.xpath('div/span[2]/a/@href')[0]
    for x in detail.xpath('//*[@id="tabInfoCont1"]/div/div[1]/div[2]/ul/li/text()'):
        f.writelines(x)
        
tree2=etree.HTML(urllib.urlopen('https://card.nonghyup.com/servlet/IPCC2012I.view').read())
cardList2= tree2.xpath('//*[@id="resultHTML"]')
for card in cardList[0].xpath('ul/li'):
    title=card.xpath('strong/span/text()')[0]
    detail= card.xpath('div/span[2]/a/@href')[0]
    for x in detail.xpath('//*[@id="tabInfoCont1"]/div/div[1]/div[2]/ul/li/text()'):
        f.writelines(x)
f.close()