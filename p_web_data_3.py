import urllib
import lxml.html
from lxml.cssselect import CSSSelector

keyword = 'python'
url = 'https://en.wikipedia.org/wiki/'+keyword
s=urllib.urlopen(url)
data=s.read()
_html = lxml.html.fromstring(data)
sel_h = CSSSelector('#mw-content-text > h2')
sel_a=CSSSelector('#mw-content-text > ul ')
results_h=sel_h(_html)
results_a=sel_a(_html)
cnt=len(results_h)
for i in range(0,cnt):
    print results_h[i].text_content()
    print results_a[i].text_content()