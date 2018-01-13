# -*- encoding= utf-8 -*-
from selenium import webdriver

# === 浏览器显示搜索结果 === #
# 搜索引擎 百度搜索 #

def search(question,driver):
        try:
            elem_s = driver.find_element_by_xpath("""//*[@id="kw"]""")
            elem_b = driver.find_element_by_xpath("""//*[@id="su"]""")
            elem_s.clear()
            elem_s.send_keys(question)
            elem_b.click()
        except:
            print("获取答案失败，如果不会，请随缘作答 (╯°Д°)╯︵ ┻━┻")

