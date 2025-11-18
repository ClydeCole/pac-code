from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select # select 下拉列表<select>

web = Chrome()
web.get("file:/home/clydecole/Desktop/python爬蟲/pac/selenium/cmd_2.py")
sel = web.find_element("xpath", '//*[@id="yearSelect"]')
sel_new = Select(sel)
with open("/home/clydecole/Desktop/python爬蟲/pac/selenium/download/books.txt", mode="w+") as f:
    for i in range(len(sel_new.options)):
        sel_new.select_by_index(i)
        trs = web.find_elements("xpath", '//*[@id="booksBody"]')
        for tr in trs:
            f.write(tr.text + "\n")

# sel_new.options # 所有的選項
# sel_new.select_by_index() # 根據位置切換
# sel_new.select_by_value() # 根據value的值切換
# sel_new.select_by_visible_text() # 根據展示的內容切換

# <select>
#     <options value="2021">2021year</options>
#     <options value="2022">2022year</options>
# <\select>


# 獲取頁面elements代碼(不是頁面源代碼，是F12裏Elements的代碼)
# page_source = web.page_source
# print(page_source)