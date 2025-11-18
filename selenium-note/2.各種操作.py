# 目標：
# 將豬八戒網站有關python 搜索結果(服務名稱、最低報價、公司名稱、服務詳情)
# 按照格式
# 文件: '服務名稱-最低報價.txt'
# 內容: '
# 公司名稱
# 服务质量评分{} - 近半年成交{} - 服务雇主数{} - 项目完成率{}
# ------
# 服務詳情'
# 進行保存



from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


def write_file(file_name ,company_name, info, content):
    with open(f"/home/clydecole/Desktop/python爬蟲/pac/selenium/download/{file_name}", "w") as f:
        f.write(f"{company_name}\n\n")
        # f.write(f"{info[1]}  {info[3]}  {info[5]}  {info[7]}\n")
        # f.write(f"{info[0]}  {info[2]}  {info[4]}  {info[6]}\n")
        f.write(f"{info[1]}: {info[0]}\n")
        f.write(f"{info[3]}: {info[2]}\n")
        f.write(f"{info[5]}: {info[4]}\n")
        f.write(f"{info[7]}: {info[6]}\n")
        f.write(f"\n--------------------------\n\n")
        f.write(f"{content}\n")


web = Chrome()
web.get("https://www.zbj.com/")


search = web.find_element("xpath", '//*[@id="j-header-searchform"]/div/input') # 找到搜索框
search.click() # 點擊搜索框
search.send_keys("python",Keys.ENTER) # 輸入python，回車

web.switch_to.window(web.window_handles[1]) # 切換窗口
divs = web.find_elements("xpath", '//div[@class="search-result-list-service"]/div') # 檢索所有項目
break_num = 0
for div in divs: # 對每一個項目進行遍歷

    # 文件名稱
    file_title = div.find_element("xpath", './/div[@class="name-pic-box"]/div/span')
    file_price = div.find_element("xpath", ".//div[@class='price']/span")
    file_name = f"{file_title.text}{file_price.text}.txt".replace("/", "-")

    # 進入詳細界面
    div.click()
    web.switch_to.window(web.window_handles[2])
    content_title = web.find_element("xpath", '//h1[@class="text-ellipsis"]')

    content_company_name = web.find_element("xpath", '//span[@class="font16 col333 font600 mr5"]') # 公司名稱

    content_company_info = web.find_elements("xpath", '//*[@id="about"]/div[2]/div[1]') # 獲得公司服務信息列表
    info_list =content_company_info[0].text.split('\n') # 會返回一個列表, 下標0,2,4,6是分數, 下標1,3,5,7是內容

    content_info_content = web.find_element("xpath", '//*[@id="intro"]/div[2]/div[1]')

    write_file(file_name, content_company_name.text, info_list, content_info_content.text)

    break

input()
