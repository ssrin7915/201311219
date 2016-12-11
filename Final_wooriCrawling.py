import urllib
from urlparse import urljoin
response=urllib.urlopen('https://sccd.wooribank.com/ccd/Dream?withyou=cd')
_html=response.read()

from lxml import etree
tree=etree.HTML(_html)
woori = "https://sccd.wooribank.com"
import codecs
f=codecs.open('WooricardBenefit.txt','w','utf-8')

cardList = tree.xpath('//*[@id="lnb"]/ul/li[2]/div/div/ul/li[1]/dl/dd/a/@href')
for card in cardList:
    url = urljoin(woori,card)
    url_tree = etree.HTML(urllib.urlopen(url).read())
    nodes = url_tree.xpath('//*[@id="content"]/div[@class="card-display-box"]/div/div/div/div/div/div[1]/div')
    for node in nodes:
        title=node.xpath('h3/text()')[0]
        details=node.xpath('div[@class="list-cd"]/ul/li/text()')
        for detail in details:
            f.write(detail)
            f.write('\n')

tree2=etree.HTML(urllib.urlopen('https://sccd.wooribank.com/ccd/Dream?withyou=CDCIF0021&CTGR_CD=C200012').read())
cardList2 = tree2.xpath('//*[@id="frm"]/div[1]/ul/li/a/@href')
for card in cardList2:
    url = urljoin(woori,card)
    url_tree = etree.HTML(urllib.urlopen(url).read())
    nodes = url_tree.xpath('//*[@id="frm"]/div[3]/div')
    for node in nodes:
        title=node.xpath('div[1]/div[2]/dl/dt/a/text()')[0]
        details=node.xpath('div[2]/ul/li/p[2]/text()')
        for detail in details:
            f.write(detail)
            f.write('\n')
f.close()