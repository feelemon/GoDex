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
        lines = file1.readlines()
        for line in lines:
            list = string.split(line)
            for word in list:
                if word == [] or word == "/":
                    list.remove(word)
                else:
                    file2.write((word + '\n').encode('utf-8'))
        return list

    convert(file1, file2)

main()
