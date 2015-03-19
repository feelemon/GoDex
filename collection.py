#!/usr/bin/python
# -*- coding: utf-8 -*-
from parsing import *
from words_list import *
from bs4 import BeautifulSoup
from pymongo import Connection

connection = Connection()
db = connection.test_database


def manage_file():
    file = open('route.txt', 'r')
    routes = file.readlines()
    for route in routes:
        collection(route)


def collection(route):
    file_site = open(str(route.rstrip('\n')), 'r')
    new_file = open("new_file.txt", "w")

    html_doc = file_site
    soup = BeautifulSoup(html_doc)

# первая итерация парсинга
    clear_script(soup, new_file)
    all_text(soup, new_file)

    file_site.close()
    new_file.close()

# вторая итерация парсинга
    text = open("new_file.txt", "r")
    new = open("new.txt", "w")

    convert(text, new)
    text.close()
    new.close()

# третий шаг - создание коллекции и запись полей
    new = open('new.txt', 'r')
    text = open("new_file.txt", "r")

    collection = {}
    collection['name'] = route.lstrip('.' '/').rstrip('\n')
    collection['route'] = route.rstrip('\n')
    collection['text'] = text.read()
    collection['features'] = new.read()
    print(collection, "\n")

# четвертый шаг - pymongo
    db.route.save(collection)
    db.route.find({}).sort([('name', 1), ('route', -1)])

if __name__ == '__main__':
    manage_file()
