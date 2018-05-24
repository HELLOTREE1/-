# -*-coding:utf-8-*-
# 使用requests库+re库爬取淘宝搜索商品页面的商品信息
import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)  # 最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    #涉及打印模板
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count+=1
        print(tplt.format(count,g[0],g[1]))
    print("")


def main():
    goods = "面膜"
    depth = 2
    # 从url连接中可以得到搜索商品的关键字是“q =”，所以我们要用的起始url为：https: // s.taobao.com / search?q = 面膜

    start_url = "https://s.taobao.com/search?q=" + goods  #
    # 翻页后，变化的关键字是s，每次翻页，s便以44的倍数增长
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
