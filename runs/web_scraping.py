from logic.scraping import Scraping
# from logic.scraping import date_f


def eluniversal_data():
    sc = Scraping()
    articles = sc.web(url='https://www.eltiempo.com/cultura/entretenimiento')
    print(articles)


eluniversal_data()
