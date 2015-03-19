# -*- coding: utf-8 -*-
import re
import sys
import string
reload(sys)
sys.setdefaultencoding('utf-8')


def convert(file_read, file_write):
    words = []
    symbol = [',' '.', '!', ')', '(', '?', ':', ';', '*', '\n', '/', '-', '+', ""]
    lines = file_read.readlines()
    for line in lines:
        list = string.split(line)
        for word in list:
            for s in symbol:
                word = word.strip(s)
            file_write.write((word + ' ').encode('utf-8'))
    return True

if __name__ == '__main__':

    text = open("new_file.txt", "r")
    new = open("new.txt", 'w')

    convert(text, new)
    text.close()
    new.close()
