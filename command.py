#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import argparse


def inputName():
    name = argparse.ArgumentParser()
    name.add_argument('-n', '--name', default='искатель')
    return name


def inputContent():
    site = argparse.ArgumentParser()
    site.add_argument('-s', '--site', default='GeekTeems, Habrahabr и Megamozg')
    return site


def inputWord():
    word = argparse.ArgumentParser()
    word.add_argument('-w', '--word', default='GeekTeems, Habrahabr и Megamozg')
    return word

if __name__ == '__main__':

    try:
        name = inputName()
        namespace = name.parse_args(sys.argv[1:])
        # print (namespace)
        print ("Привет, {}!".format(namespace.name))
    except Exception:
        print('Это что ещё такое?')
    else:
        try:
            site = inputContent()
            sitespace = site.parse_args(sys.argv[1:])
            print("Будем искать на {}!".format(sitespace.site))
        except Exception:
            print('Это что ещё такое?')
        else:
            try:
                word = inputContent()
                wordspace = word.parse_args(sys.argv[1:])
                print("Будем искать на {}!".format(wordspace.word))
            except Exception:
                print('Это что ещё такое?')
            else:
                print('Сейчас найдем...')
