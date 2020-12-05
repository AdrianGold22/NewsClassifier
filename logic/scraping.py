import requests
import urllib.request
from bs4 import BeautifulSoup
import datetime

fieldnames = ['title', 'content', 'type']
sources = ["Sinc", "Expansion", "Reforma", "El Universal", "El Mundo", "BBC Mundo", "ONU News", "El periodico deportivo", "Investigacion y ciencia", "Marca", "Sport", "Informador.mx", "ABC.es", "La Vanguardia"]
date_f = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")


class Scraping(object):
    """ Class used scraping resources"""
    @staticmethod
    def rss(url: str = '') -> list:
        article_list = []
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, features='xml')
            articles = soup.findAll('item')
            for a in articles:
                title = a.find('title').text
                link = a.find('link').text
                description = a.find('description').text
                published = a.find('pubDate').text
                article = {
                    'title': title,
                    'link': link,
                    'description': description,
                    'published': published,
                    'items': soup.findAll('item')
                    }
                article_list.append(article)
            return article_list
        except Exception as e:
            print('The scraping rss job failed. {0}'.format(e))
            return list()

    @staticmethod
    def web(url: str) -> list:
        try:
            parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
            resp = urllib.request.urlopen(url)
            soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
            links = list()
            for row in soup.find_all('a', href=True):
                path = str(row['href'])
                print(path)
                if path.find('/') == 0 and path.count('/') >= 1:
                    if (url + path) not in links:
                        links.append(url + path)
            print(links)
            return links

        except Exception as e:
            print('The scraping web job failed. {0}'.format(e))
            return list()
