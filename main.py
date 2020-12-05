import os

from root import DIR_INPUT
from runs.rss_scraping import rss_scrap, urls


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def initial_path():
    if len(os.listdir(DIR_INPUT)) == 0:
        print("Empty")
        dir_path = rss_scrap(urls, 'Es_News')
    else:
        dir_path = DIR_INPUT + 'Es_News_report.csv'

    return dir_path

