# -*- coding: utf-8 -*-
import sys
import os
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


def clear_script(soup, file):
    for i in soup.find_all('script'):
        i.replaceWith('')
    return True


def all_text(soup, file):
    text = soup.get_text()
    for item in text:
        if item.encode('utf8'):
            file.write(item.encode('utf8'))
    return True


def _os_walk(path='./'):
    file = open("route.txt", "w")
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            file.write(os.path.join(root, name) + "\n")
    return True

if __name__ == '__main__':

    file_site = open("index.html", "r")
    new_file = open("new_file.txt", "w")
    html_doc = file_site
    soup = BeautifulSoup(html_doc)

    clear_script(soup, new_file)
    all_text(soup, new_file)
    _os_walk()
    file_site.close()
    new_file.close()
