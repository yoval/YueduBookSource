# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:52:44 2021

@author: fuwen

从备份文件中提取书源
"""
import os,re,json
from tld import get_tld

# 打开分享书源
f=open('shareBookSource.json',encoding='utf-8')
f=f.read()
comment = re.compile('(  {.*?\n  })',re.DOTALL)
JsonList = comment.findall(f)

# 创建工作目录
WorkDir = 'SingleBookSource'
if not os.path.exists(WorkDir):
    os.makedirs(WorkDir)

DomainNames = []
for JsonText in JsonList :
    Json = json.loads(JsonText)
    NovelUrl = Json['bookSourceUrl']
    NovelUrl = NovelUrl.split(' ')[0]
    try:
        Result = get_tld(NovelUrl, as_object=True,fix_protocol=True)
    except :
        try :
            SearchUrl = Json['searchUrl']
            Result = get_tld(SearchUrl, as_object=True,fix_protocol=True)
        except :
            try:
                ExploreUrl=Json['exploreUrl']
                ExploreUrl=re.search("(?P<url>https?://[^\s]+)", ExploreUrl).group("url")
                Result = get_tld(ExploreUrl, as_object=True,fix_protocol=True)
            except:
                continue
    DomainName = Result.fld
    DomainNames.append(DomainName)
    if os.path.isfile('%s\%s.json'%(WorkDir,DomainName)):
        print('文件已存在，跳过')
        continue
    else :
        print('文件不存在，新建')
        with open('%s\%s.json'%(WorkDir,DomainName),'w',encoding='utf-8') as f:
            f.write('['+JsonText+']')       
DomainNames = list(set(DomainNames)) 
for DomainName in DomainNames:
    with open('DomainName.txt','a') as d:
        d.write(DomainName+'\n\n')
