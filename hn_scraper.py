import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links,  subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score') 
        # print(f'printing subtext[idx]: {subtext[idx]}')
        # print(f'printing vote: {vote}')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            #Filter stories with over 100 votes
            if points > 100: 
                hn.append({'title': title, 'link': href, 'votes': points})
                print(points)
    return hn

pprint.pprint(sort_stories_by_votes(create_custom_hn(links, subtext)))
