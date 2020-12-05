import os
from root import DIR_INPUT
from runs.rss_scraping import rss_scrap, urls


def initial_path(file_name):
    dir_path = DIR_INPUT + '{0}.csv'.format(file_name)
    if os.path.exists(dir_path):
        print('Found it')
    else:
        print('File {0} not found. Starting RSS scraping...'.format(file_name))
        dir_path = rss_scrap(urls, file_name)

    return dir_path


# initial_path('ElUniversal_News_report')
