import urllib
from urlparse import urljoin
import codecs
response=urllib.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/propose/propose.jsp')
_html=response.read()

from lxml import etree
tree=etree.HTML(_html)
shinhan='https://www.shinhancard.com'

pages = tree.xpath('//*[@id="pbContent"]/div[@class="tabWrap1"]/ul/li/ul/li/a/@href')

f=codecs.open('SinhancardBenefit.txt','w','utf-8')
for page in pages:
    url = urljoin(shinhan,page)
    url_tree = etree.HTML(urllib.urlopen(url).read())
    nodes = url_tree.xpath('//*[@id="pbContent"]/div[@class="cardList"]')
    for node in nodes:
        title=node.xpath('div[@class="cardName"]/strong/text()')[0]
        detail=node.xpath('div[@class="btn"]/a[@class="btnCardWhite"]/@href')[0]
        detail_url = urljoin(shinhan,detail)
        detail_tree = etree.HTML(urllib.urlopen(detail_url).read())
        for x in detail_tree.xpath('//*[@id="pbTabDepth1-1"]/div'):
            for benefit in x.xpath('p/text()'):
                f.write(benefit) 
                f.write('\n')
f.close()