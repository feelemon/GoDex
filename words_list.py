import sys
import string
reload(sys)
sys.setdefaultencoding('utf-8')


def main():

    text = open("new_file.txt", "r")
    new = open("new.txt", "w")

    functions(text, new)
    text.close()
    new.close()


def functions(file1, file2):

    def convert(file1, file2):
        symbol = [',' '.', '!', ')', '(', '?', ':', ';', '*', '\n', '/', '-', '+']
        lines = file1.readlines()
        for line in lines:
            list = string.split(line)
            for word in list:
                for i in symbol:
                    word = word.strip(i)
                file2.write((word + '\n').encode('utf-8'))
                print(word)
        return list

    convert(file1, file2)

main()
