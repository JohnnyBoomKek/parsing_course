"""
1.Parse webpage
2.Find all links
3.asynchronously get info from every link

Bonus:
Do the it syncronously and compere the results

assumtions:
 - every given URL is valid
"""

from sys import path_importer_cache
import time
from bs4 import BeautifulSoup
import requests
import aiohttp
import validators
import asyncio
import json
import csv 

def get_all_links(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    anchors = soup.find_all('a')
    urls = []
    for anchor in anchors:
        link = anchor.get('href')
        if validators.url(link):
            urls.append(link)
    return urls

links = get_all_links('http://wordpress.org')

async def get_url_info(url, session):
    async with session.get(url) as response:
        print('getting data from', url)
        data = await response.read()
        return json.loads(data.decode('utf-8'))

async def main(links):
    url = 'https://api.domainsdb.info/v1/domains/search?domain='
    tasks = []

    async with aiohttp.ClientSession() as session:
        for link in links:
            print(link)
            task = asyncio.create_task(get_url_info(url+link, session))
            tasks.append(task)

        await asyncio.gather(*tasks)
        return [task.result() for task in tasks]

"""
Hard skills
Amount of people 
"""
result = asyncio.run(main(links))