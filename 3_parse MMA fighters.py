"""
Parse every mma fighter from espn.com
"""

from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup
import csv
import string 

ABCS = string.ascii_lowercase 

def to_csv(data, name):
    with open(f'{name}.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data[key] for key in data.keys()])

def get_html(url):
    return requests.get(url).text

def get_bio(url):
    soup = BeautifulSoup(get_html(url), 'lxml')
    divs = soup.find_all('ul')
    fighter_bio = {}
    for div in divs:
        if div.get('class') and "PlayerHeader__Bio_List" in div.get('class'):
            bio = div
    if bio:
        for li in bio.find_all('li'):
            for div in li.find_all('div', class_='ttu'):
                fighter_bio[div.text]=div.find_next().text
    return fighter_bio

def get_list_of_fighters(html):
    list_of_fighters = []
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find_all('tr')[2:]
    fighter_data = dict()
#    fighter_data = {
        #'Name':None,
        #'URL': None,
        #'Country':None,
        #'DOB':None,
        #'Team':None,
        #'Stance':None,
        #'HT/WT': None,
        #'Reach':None,
        #'Nickname':None,

    #}
    for tr in trs:
        fighter = tr.find_all('td')[0]
        url = 'https://www.espn.com' + fighter.find('a').get('href')
        country = tr.find_all('td')[1]
        fighter_data['Name']=fighter.text
        fighter_data['URL'] = url
        fighter_data['Country']=country.text
        to_csv(fighter_data, 'fighers')

    

def main():
    for letter in ABCS:
        url = f"http://www.espn.com/mma/fighters?search={letter}"
        get_list_of_fighters(get_html(url))

if __name__ == '__main__':
    main()