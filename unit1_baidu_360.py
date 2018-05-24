#-*-coding:utf-8-*-
import requests
keywords="Python"
try:

    kv={'wd':'Python'}
    r=requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("failure")
