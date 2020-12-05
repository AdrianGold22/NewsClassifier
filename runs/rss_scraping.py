import re
from logic.getindata import initial_data
from logic.scraping import Scraping
from logic.scraping import date_f

urls = {
    'Ciencia y Tecnologia': ['https://www.agenciasinc.es/feed/Ciencias', 'https://www.agenciasinc.es/feed/Tecnologia', 'http://feeds.feedburner.com/cienciamx/mmzD?format=xml', 'https://www.investigacionyciencia.es/rss/noticias', 'http://www.bbc.co.uk/mundo/temas/ciencia/index.xml', 'http://www.elmundo.com/images/rss/vida_ciencia.xml', 'https://www.eluniversal.com.co/rss/ciencia.xml', 'http://feeds.feedburner.com/cienciamx/bTrQ?format=xml', 'http://www.bbc.co.uk/mundo/temas/tecnologia/index.xml', 'http://www.elmundo.com/images/rss/vida_tecnologia.xml', 'https://www.eluniversal.com.co/rss/tecnologia.xml'],
    'Deportes': ['https://www.sport.es/es/rss/deportes/rss.xml', 'https://www.sport.es/es/rss/nba/rss.xml', 'https://e00-marca.uecdn.es/rss/portada.xml','https://www.informador.mx/rss/deportes.xml','https://elperiodicodeportivo.com.co/rss.xml', 'http://www.elmundo.com/images/rss/deportes.xml', 'https://www.elmundo.com/images/rss/deportes_mundo_deportivo.xml', 'https://www.eluniversal.com.co/rss/deportes.xml'],
    'Economia': ['https://www.informador.mx/rss/empresas.xml', 'https://www.reforma.com/rss/negocios.xml', 'https://expansion.mx/rss/empresas', 'https://expansion.mx/rss/emprendedores','https://expansion.mx/rss/dinero', 'https://expansion.mx/rss/economia', 'https://news.un.org/feed/subscribe/es/news/topic/economic-development/feed/rss.xml', 'http://www.bbc.co.uk/mundo/temas/economia/index.xml', 'http://www.elmundo.com/images/rss/noticias_economia.xml'],
    'Salud': ['https://www.lavanguardia.com/mvc/feed/rss/vida/salud', 'https://www.agenciasinc.es/feed/Salud', 'https://www.abc.es/rss/feeds/abc_SociedadSalud.xml'],
    'Cultura': ['https://www.informador.mx/rss/entretenimiento.xml', 'https://www.reforma.com/rss/gente.xml', 'https://www.reforma.com/rss/cultura.xml', 'https://www.agenciasinc.es/feed/Sociedad', 'https://news.un.org/feed/subscribe/es/news/topic/culture-and-education/feed/rss.xml', 'http://www.bbc.co.uk/mundo/temas/cultura/index.xml', 'http://www.elmundo.com/images/rss/cultura.xml', 'https://www.elmundo.com/images/rss/cultura_cultural.xml', 'https://www.eluniversal.com.co/rss/farandula.xml']
}


def rss_scrap(urls_n, font):
    sc = Scraping()
    links = []
    for url in urls_n:
        link_type = urls_n[url]
        for link_base in link_type:
            resp = sc.rss(url=link_base)
            for i in resp:
                items = i['items']
                for j in items:
                    link = j.findAll('link')
                    first_link = re.findall('http.+<', str(link[0]))
                    list_links = first_link[0].split('<')
                    links.append([list_links[0], url])
    return initial_data(font, links)


# data_location = rss_scrap(urls, 'ES_News')
# print(data_location)


