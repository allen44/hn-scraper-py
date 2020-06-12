import requests
from bs4 import BeautifulSoup
import pprint

def request_hn_data(url, page_number):
    page_number = str(1)
    combined_url =  url + page_number
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    return res, soup, links, subtext

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn():
    hn = []
    for page_num in range(3): #scrape three pages
        res, soup, links, subtext = request_hn_data(url, page_num)
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

url = 'https://news.ycombinator.com/news?p='

pprint.pprint(sort_stories_by_votes(create_custom_hn()))
