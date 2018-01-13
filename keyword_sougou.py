# -*- encoding= utf-8 -*-
import requests
from bs4 import BeautifulSoup

# === 获取搜索结果的关键字 === #
# 搜索引擎 搜狗搜索 #

def search(question):
    h_url = 'https://www.sogou.com/sogou?query='
    a_url = h_url+str(question)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
        }
        r = requests.get(a_url, headers=headers)
        r.encoding = 'utf-8'  # 网页源码HEAD中可以查看
        soup = BeautifulSoup(r.text, 'html.parser')       
        answer = soup.find('div', attrs='str-text-info')
        keywords = answer.find_all('em')
        for keyword in keywords:
            print(keyword.contents[1])
    except:
        print("获取答案失败，如果不会，请随缘作答 (╯°Д°)╯︵ ┻━┻")

