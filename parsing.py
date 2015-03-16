import sys
import os
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


def main():
    file_site = open("index.html", "r")
    new_file = open("new_file.txt", "w")
    html_doc = file_site
    soup = BeautifulSoup(html_doc)

    functions(soup, new_file)
    file_site.close()
    new_file.close()


def functions(soup, file):

    def title_text(soup, file):
        file.write(soup.title.string.encode('utf8'))

    def clear_script(soup, file):
        for i in soup.find_all('script'):
            i.replaceWith('')

    def all_text(soup, file):
        text = soup.get_text()
        for item in text:
            if item.encode('utf8'):
                file.write(item.encode('utf8'))

    def _os_walk(path='./'):
        for root, dirs, files in os.walk(".", topdown=True):
            for name in files:
                print(os.path.join(root, name))

    title_text(soup, file)
    clear_script(soup, file)
    all_text(soup, file)
    _os_walk()

main()
