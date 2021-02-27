"""
Reading and Writing from and to CSV
"""

import csv


# Having a dict we can write its values like so:
def write_csv(data:dict):
    with open('names.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data['key1'], data['key2']) # use actual keys


# The method below is used to write dict values supposedly more conviniently 
def write_csv(data:dict):
    with open('names.csv', 'a') as file:
        order = ['key1', 'key2'] #etc
        dict_writer = csv.DictWriter(file, fieldnames=order)

        dict_writer.writerow(data)

#csv reader 
def read_csv(filename:str):
    with open(filename) as file:
        fieldnames = ['key1', 'key2'] #etc
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            
            pass 