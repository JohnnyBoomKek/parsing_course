import requests
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def to_csv(data,filename, fieldnames):
    with open(filename, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)

def corrected_data(data:str):
    r = data.strip().split('\n')[1:]
    data = []
    for col in r:
        col = col.split('\t')
        result = {}
        result['name'] = col[0]
        result['slogan'] = col[2]
        result['clicks'] = col[3]
        data.append(result)
    return data

def main():
    page = 1
    url = f'https://www.liveinternet.ru/rating/ru/internet/today.tsv?page={page}'
    for page in range(10):
        data = get_html(url)
        data = corrected_data(data)
        for row in data:
            to_csv(row, 'websites.csv', ['name', 'slogan', 'clicks'])

if __name__ == '__main__':
    main()