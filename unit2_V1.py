#-*-coding:utf-8-*-
#大学排名ＵＲＬ链接
# ＃定向爬虫
# １从网络获取大学排名
# ２提取网页信息
# ３了利用数据结构展示并且输出结果
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#过滤费标签
            tds=tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
    pass

def printUnivList(ulist,num):
    # print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))#chr(12288)中文空格
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    # print("successful"+str(num))

def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,40)
main()