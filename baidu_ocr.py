# -*- encoding= utf-8 -*-
from PIL import Image
import requests
import base64
import os
import time
#from selenium import webdriver # 如果使用result_selenium请将这条语句前面的#删除
from reasult_baidu import search # 改变搜索方法的格式: from (方法文件名) import search


client_id = input("输入你的API Key：")
client_secrt = input("输入你的Scret Key：") 
token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+str(client_id)+'&client_secret='+str(client_secrt)
access_token_url = requests.get(token_url).json()
access_token = access_token_url['access_token'] #  access_token是获取一次就可以使用三十天的，为了方便可以在获取后将前面的代码注释掉，直接赋值这条语句

dr_url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(dr_url)
# 如果需要使用result_selenium请将这条语句前面的三行的#删除

while 1:
    yn = input("答题开始？是输入y，否输入n：")
    start = time.time()
    if yn == 'y':
        if not os.path.exists("screenshots/"):
            os.mkdir("screenshots/")
        t = "%d%d%d%d%d%d" % time.localtime()[0:6]
        os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
        os.system("adb pull /sdcard/screenshot.png C:/Users/Administrator/Desktop/AnswerHelper/screenshots/"+t+".png")#图片地址自己改，我的这个不一定适用你的电脑
        ima = Image.open('screenshots/'+t+'.png')
        ima2 = ima.crop((60,300,1000,570)) #  cool1 dual
        path = 'screenshots/'+t+'_f.png'
        ima2.save(path)
        with open(path, 'rb') as f:
            image_data = f.read()
            base64_ima = base64.b64encode(image_data)
        data = {
            'image': base64_ima
            }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token="+str(access_token)
        r = requests.post(url, params=headers, data=data).json()
        que = ""
        for word in r['words_result']:
            que += word['words']
        print(que)
        search(que) # 如果使用result_selenium请换成 search(que, driver)
    overt = time.time()
    print(str(overt-start)+"s")



