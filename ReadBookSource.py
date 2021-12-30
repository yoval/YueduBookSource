# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 02:31:41 2021

@author: fuwen

"""
import json,re,itertools


NewBookSourcePath = r'D:\Code\YueduBookSource\NewBookSource.json'
File = open(NewBookSourcePath,'r', encoding='utf-8')

def remove_control_chars(s):
    control_chars = ''.join(map(chr, itertools.chain(range(0x00, 0x20), range(0x7f, 0xa0))))
    control_char_re = re.compile('[%s]' % re.escape(control_chars))
    return control_char_re.sub('', s)

FileText = File.read()
JsonList = json.loads(FileText)
for Json in JsonList:
    bookSourceName = Json['bookSourceName']
    bookSourceName = remove_control_chars(bookSourceName)
    bookSourceUrl = Json['bookSourceUrl']
    with open('WebSite.md','a', encoding='utf-8') as f:
        f.write('|' + bookSourceName + '|' + bookSourceUrl + '|\n')


