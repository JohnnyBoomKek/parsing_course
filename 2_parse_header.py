#спарсим несколько заголовков и запишим в csv 
import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    html = requests.get(url)
    return html.text

def refined(s):
    return s.replace(',', '').split()[0][1:]

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    featured_plugins = soup.find_all('section')[1]
    plugins = featured_plugins.find_all('article')
    for plugin in plugins:
        name = plugin.find('h3', class_='entry-title').text
        url = plugin.find('h3', class_='entry-title').find('a').get('href')
        ratings = refined(plugin.find('span', class_='rating-count').text)
        data = {
            'name':name,
            'url': url,
            'ratings':ratings,
        }
        to_csv(data)

def to_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['url'], data['ratings']))

def main():
    get_data(get_html(url))

if __name__ == '__main__':
    url = 'https://wordpress.org/plugins/'
    main()