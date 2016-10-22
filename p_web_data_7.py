import requests
import lxml.html
from lxml.cssselect import CSSSelector

url='http://www.bbc.co.uk/sport/football/premier-league/results'
r=requests.get(url)
_html=r.text
html=lxml.html.fromstring(_html)
sel=CSSSelector('#results-data > table')
results=sel(html)

home_team=CSSSelector('td.match-details > p > span.team-home.teams')
score=CSSSelector('td.match-details > p > span.score')
away_team=CSSSelector('td.match-details > p > span.team-away.teams')

for result in results:
    _home_team=home_team(result)
    _score=score(result)
    _away_team=away_team(result)
    for i in range(0,len(_home_team)):
        print _home_team[i].text_content().strip() ,
        print  _score[i].text_content().split('-')[0] ,
        print  _score[i].text_content().split('-')[1] ,
        print _away_team[i].text_content().strip()