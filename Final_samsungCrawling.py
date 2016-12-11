import urllib
from urlparse import urljoin
from lxml import etree
import codecs

f=codecs.open('SamsungcardBenefit.txt','w','utf-8')
samsung = "https://www.samsungcard.com"
tree=etree.HTML(urllib.urlopen('https://www.samsungcard.com/personal/card/digital/UHPPCC0388M0.jsp').read())
cardList = tree.xpath('//*[@id="contents"]/div/div[3]/ul/li')
for card in cardList:
    title=card.xpath('div/a[1]/span[1]/text()')[0]
    detail=card.xpath('div/a[1]/@href')[0]
    detail_url = urljoin(samsung,detail)
    detail_tree = etree.HTML(urllib.urlopen(detail_url).read())
    for detail in detail_tree.xpath('//*[@id="benefit00"]/ul/li'):
        for benefit in detail.xpath('a/dl/dd/div/ul/li/span/text()'):
            f.write(benefit)
            f.write('\n')

tree2=etree.HTML(urllib.urlopen('https://www.samsungcard.com/personal/card/number/UHPPCA0202M0.jsp').read())
cardList2 =tree2.xpath('//*[@id="contents"]/div/div/div/ul/li')
for card in cardList2:
    for detail in card.xpath('div/ul/li'):
        title=detail.xpath('div[2]/p/a/text()')[0]    
        url=detail.xpath('div[2]/div/a[1]/@href')[0]
        detail_url = urljoin(samsung,url)
        detail_tree = etree.HTML(urllib.urlopen(detail_url).read())
        for x in detail_tree.xpath('//*[@id="benefit00"]/ul/li'):
            for benefit in x.xpath('a/dl/dd/div/ul/li/span/text()'):             
                f.write(benefit)
                f.write('\n')


tree3=etree.HTML(urllib.urlopen('https://www.samsungcard.com/personal/card/check-card/UHPPCA0206M0.jsp').read())
cardList3 =tree3.xpath('//*[@id="card_append"]/li')
for card in cardList3:
    title = card.xpath('dl/dt/a/text()')[0]
    detail = card.xpath('dl/dd[2]/a/@href')[0]
    detail_url="https://www.samsungcard.com/personal/card/cardfinder/UHPPCA0102M0.jsp?code="+detail[25:32]
    detail_tree = etree.HTML(urllib.urlopen(detail_url).read())
    for x in detail_tree.xpath('//*[@id="benefit00"]/ul/li'):
        for benefit in x.xpath('a/dl/dd/div/ul/li/span/text()'):        
            f.write(benefit)
            f.write('\n')
       
f.close()