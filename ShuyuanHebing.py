# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:46:23 2021
@author: fuwen
"""
import os

WorkDir = 'SingleBookSource'
FileNameList = os.listdir(WorkDir) 
for FileName in FileNameList:
    FileText = open('%s\%s'%(WorkDir,FileName),encoding='utf-8')
    FileText = FileText.read()
    FileText = FileText[1:-1]
    FileText = FileText+',\n'
    with open('BookSource.json','a',encoding='utf-8') as f:
        f.write(FileText)
SourceText = open('BookSource.json',encoding='utf-8')
SourceText = SourceText.read()
with open('BookSource.json','w',encoding='utf-8') as g:
    g.write('['+SourceText+']')