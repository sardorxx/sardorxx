import requests
import codecs
from bs4 import BeautifulSoup

lang = 'en'
base_url = f'https://kun.uz/{lang}'
data = requests.get(url=base_url)

soup = BeautifulSoup(data.text, 'html.parser')

categories_link = soup.find_all('a', attrs='menu-link')
categories_link = [{f'{c.text}': c['href'][3:]} for c in categories_link]


def category_articles(links, base_url):
    result_links = []
    for link in links:
        data = requests.get(url=base_url + list(link.values())[0])
        soup = BeautifulSoup(data.text, 'html.parser')
        articles = soup.find_all('a', attrs='small-news__title')
        result_links.append({list(link.keys())[0]: [article['href'][3:] for article in articles]})
    a = """ """
    for i in result_links:
        a += (str(list(i.keys())[0])) + '\n'
        for j in i.values():
            for m in j:
                datas = requests.get(url=base_url+m)
                soups = BeautifulSoup(datas.text, 'html.parser')
                paras = soups.find_all('p')
                text_paras = [p.text for p in paras]
                a += str(text_paras) + '\n'
    print(a)
    with codecs.open('kun_uz_sardor.txt', 'w', 'utf-8-sig') as f:
        f.write("".join(a))


category_articles(categories_link, base_url)
