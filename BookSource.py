# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 02:31:41 2021

@author: fuwen

"""
from bs4 import BeautifulSoup
import json,requests,tld

#阅读APP导出书源
SharePath = r'D:\OneDrive\YueduBookSource\yck\yck.json'



#标题含有以下字符删除
WordList = ['BadRequest','503','login','Attention','Error','404','Apache','Cloudflare','baidu','公益','提示','漫画','升级','安全','200','Apache','Found','Spring']

def GetMainUrl(url):
    hea = url.split('/')[0]
    try:
        obj = tld.get_tld(url,as_object=True)
    except:
        return 'http:'
    if obj.subdomain =='':
        Domain =hea + '//'+ obj.fld
    else:
        Domain = hea + '//' + obj.subdomain +'.'+ obj.fld
    return Domain


def Rename(title):
    title = title.replace(' ','')
    title = title.replace('\n','')
    title = title.split('-')[0]
    title = title.split('－')[0]
    title = title.split('|')[0]
    title = title.split('_')[0]
    title = title.split('—')[0]
    title = title.split(',')[0]
    title = title.split('―')[0]
    title = title.split('，')[0]
    return title

headers = {'User-Agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'}
File = open(SharePath,'r', encoding='utf-8')
FileText = File.read()
JsonList = json.loads(FileText)
NewJsonList = []
Len =len(JsonList)
count = 0
for Json in JsonList:
    print(Len-count)
    count+=1
    #删除有声小说书源
    if Json['bookSourceType']==1:
        continue
    WebUrl = Json['bookSourceUrl']
    WebUrl = GetMainUrl(WebUrl)
    Json['bookSourceUrl']=WebUrl
    #删除连接不上的书源
    try:
        rep = requests.get(WebUrl,headers = headers,timeout=10)
    except:
        continue
    rep.encoding = rep.apparent_encoding
    Soup = BeautifulSoup(rep.text,'html.parser')
    try:
        Title = Soup.title.string
        Title = Rename(Title)
    except:
        continue
    #修改标题
    Json['bookSourceName'] = Title
    #删除网站名称含关键词源
    Isin = [i in Title for i in WordList]
    if any(Isin):
        continue
    Json['bookSourceComment'] =''
    Json['bookSourceGroup'] =''
    NewJsonList.append(Json)
NewJsonText = json.dumps(NewJsonList)

with open('NewBookSource.json','w') as f:
    json.dump(NewJsonList,f)