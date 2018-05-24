#-*-coding:utf-8-*-
import requests

def getHTMLText(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}  # Mozilla/5.0浏览器的身份标识 通过改变ｈｅａｄｅｒ模拟浏览器
        r=requests.get(url,headers=kv)
        r.raise_for_status()#如果不是200，引发HTTPError异常
        r.encoding=r.apparent_encoding
        return r.text[1000:2000]
    except:
        return "产生异常"

if __name__=="__main__":
    url="https://www.amazon.cn/gp/product/B01M8L5z3Y"
    print(getHTMLText(url))