"""
Challenge
Take data from a csv file and pass it to a postgres database
"""

import csv 
from peewee import *

db = PostgresqlDatabase(database='test', user='postgres', password='1234', host='localhost')

class Fighter(Model):
    name = CharField()
    url = CharField()
    country = CharField()    

    class Meta:
        database = db


def read_csv(filename:str, fieldnames:list):
    with open(filename) as file:
        reader = csv.DictReader(file, fieldnames=fieldnames)
        return list(reader)




def main():
    db.connect()
    db.create_tables([Fighter]) 
    reader = read_csv('fighers.csv', ['name', 'url', 'country'])
    with db.atomic():
        for index in range(0, len(reader), 1000):
            Fighter.insert_many(reader[index:index+1000]).execute()
            print(index, 'fighters were added')

if __name__ == '__main__':
    main()
