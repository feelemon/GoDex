import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


def main():
    file_site = open("index.html", "r").read()
    new_file = open("new_file.txt", "w")
    html_doc = file_site
    soup = BeautifulSoup(html_doc)

    function(soup, new_file)


def function(soup, file):

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

    def parsing_links(soup, file):
        links = soup.find_all('a')
        for link in links:
            file.write(link.get('href') + "\n")

    title_text(soup, file)
    clear_script(soup, file)
    all_text(soup, file)
    parsing_links(soup, file)

main()
