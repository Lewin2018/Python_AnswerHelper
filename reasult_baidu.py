# -*- encoding= utf-8 -*-
import requests
from bs4 import BeautifulSoup

# === 获取搜索结果的摘要 === #
# 搜索引擎 百度搜索 #

def search(question):
    h_url = 'https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word='
    a_url = h_url+str(question)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
        }
        r = requests.get(a_url, headers=headers)
        r.encoding = 'GBK'  # 网页源码HEAD中可以查看
        soup = BeautifulSoup(r.text, 'html.parser')
        answer_list = soup.find_all('dd', attrs='dd answer' ,limit=3)  # limit参数可自行调整，为答案显示数量
        num = 0
        for answer in answer_list:
            num += 1
            ans = ""
            for x in answer.contents:
                ans += str(x.string)
            print(str(num) + "、" + ans)
    except:
        print("获取答案失败，如果不会，请随缘作答 (╯°Д°)╯︵ ┻━┻")

