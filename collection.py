import pymongo
import parsing.py
import words_list.py
from bs4 import BeautifulSoup
from pymongo import Connection


def connections():
    connection = Connection()
    db = connection.test_database


def manage_file():
    file = open('route.txt', 'r')
    routes = file.readlines()
    for route in routes:
        collection(route)


def collection(route):
    file_site = open(str(route), '+')
    new_file = open("new_file.txt", "+")

    html_doc = file_site
    soup = BeautifulSoup(html_doc)

# первая итерация бабах
    clear_script(soup, new_file)
    all_text(soup, new_file)

    file_site.close()
    new_file.close()

# вторая итерация бадунтсс
    text = open("new_file.txt", "+")
    new = open("new.txt", "+")

    convert(text, new)

# третий шаг - запихивание в коллекцию бабах
    collection = {}
    collection[name] = route
    collection[route] = route
    collection[text] = text.read()
    collection[features] = new.read()
    print(collection)

# четвертый шаг - pymongo
    db.route.insert(collection)
    db.route.save(user)
    db.route.find({}).sort([('name', 1), ('route', -1)])

if __name__ == '__main__':
    connection()
    manage_file()
