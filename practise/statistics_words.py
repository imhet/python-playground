#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# statistics words in text files


def is_chinese(uchar):
    """????unicode?????"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_alphabet(uchar):
    """ ????unicode??????? """
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False


def is_number(uchar):
    """????unicode?????"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False


f = open('test/words')

for line in f:
    words = line.split()
    for w in words:
        if is_alphabet(w):
            print(w)

