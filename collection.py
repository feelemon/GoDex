# -*- coding: utf-8 -*-
from parsing import *
from words_list import *
from bs4 import BeautifulSoup
from pymongo import Connection

connection = Connection()
db = connection.test_database


def manage_file():
    file = open('route.txt', 'w')
    file = open('route.txt', 'r')
    # предварительно проверим наличие файлов:
    os_walk()
    routes = file.readlines()
    for route in routes:
        # проверим страничка ли это:
        if route[len(route) - 5: len(route)].strip('\n') == 'html':
            collection(route)
    file.close()


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
    collection['NAME'] = route.lstrip('.' '/').rstrip('\n')
    collection['ROUTE'] = route.rstrip('\n')
    collection['TEXT'] = text.read()
    collection['FEATURES'] = new.read()

    new.close()
    text.close()

# четвертый шаг - pymongo
    db.route.save(collection)
    db.route.find({}).sort([('NAME', 1), ('ROUTE', -1)])

if __name__ == '__main__':
    manage_file()
