import os
import time
from tqdm import tqdm
from logic.scraping import fieldnames, sources
from root import DIR_INPUT
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as Bs
import requests


def unique_rows(a):
    """
    :Date: 2020-09-14
    :Author: user545424
    :webpage: https://stackoverflow.com/questions/8560440/removing-duplicate-columns-and-rows-from-a-numpy-2d-array
    """
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)] * a.shape[1]))
    return np.array(unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1])))


def initial_data(file_input, list_links):
    file_report = '{0}_report.csv'.format(file_input)
    data_input = DIR_INPUT + file_report
    np_links = unique_rows(np.array(list_links))
    data = []
    print("\nSources: {0}".format(', '.join(sources)))
    try:
        print('Initial data input in {0} loading {1}...'.format(file_input, len(np_links[:, 0])))
        for page in tqdm(range(len(np_links[:, 0]))):
            r = requests.get(np_links[page, 0])
            soup = Bs(r.content, 'html.parser')
            title = soup.title
            if title is not None:
                title = title.text
                typo = str(np_links[page, 1])
                content_element = soup.find_all('p')
                for content in content_element:
                    n_content = content.find_all('p')
                    # print(content)
                    if len(n_content) != 0:
                        content_element.remove(content)
                for i in n_content:
                    content_element.append(i)

                content_element = set(content_element)
                content_text = [element.text for element in content_element]
                content_text = ' '.join(content_text)
                content_text = content_text.rstrip('\n')
                # print(content_text, '\n')
                if content_text != '':
                    row = [title, content_text, typo]
                    # print({'title': title, 'type': typo})
                    data.append(row)
            else:
                continue
        print('Final data input in {0} loading {1}...'.format(file_input, len(data)))
        print('Data input for {0} save successful!'.format(file_input))
    except Exception as e:
        print('The scraping web job failed. {0}'.format(e))

    df = pd.DataFrame(data, columns=fieldnames)
    df.to_csv(data_input, index=None, mode="a", header=not os.path.isfile(data_input), sep=';', encoding="utf-8")
    counting = df['type'].value_counts()
    print("")

    print(counting)
    return data_input
