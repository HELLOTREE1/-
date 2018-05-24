#-*-coding:utf-8-*-
import requests
import os

root="/home/szu/Pictures/MARK//"
url="https://www.nationalgeographic.com/content/dam/travel/photos/000/348/34817.ngsversion.1483651823948.adapt.676.1.jpg"
path= root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("file saved successfully")
    else:
        print("file already exists")
except:
    print("failure")