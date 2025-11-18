from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

# 配置無頭信息
from selenium.webdriver.chrome.options import Options
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt)
web.get("file:/home/clydecole/Desktop/python爬蟲/pac/selenium/cmd_2.py")
sel = web.find_element("xpath", '//*[@id="yearSelect"]')
sel_new = Select(sel)
with open("/home/clydecole/Desktop/python爬蟲/pac/selenium/download/books.txt", mode="w+") as f:
    for i in range(len(sel_new.options)):
        sel_new.select_by_index(i)
        trs = web.find_elements("xpath", '//*[@id="booksBody"]')
        for tr in trs:
            print(tr.text)