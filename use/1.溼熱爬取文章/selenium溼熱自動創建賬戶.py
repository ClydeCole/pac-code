import json
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# ---------- config ----------
url1 = "https://shireyishunjian.com" # 頂級域名
url2 = "https://www.shireyishunjian.com/main/member.php?mod=register" # 註冊賬戶
url3 = "https://www.shireyishunjian.com/main/portal.php?mod=index&mobile=no" # 賬戶主頁
url4 = "https://www.shireyishunjian.com/main/questionnaire/" # 問卷

user_name = []
pass_word = []
user_mail = []
qq_num = 1231231
# print(len(user_name))
# print(len(pass_word))
# print(len(email))
# print(len(qq_num))

# ---------- config ----------



def login_account(url, username, password):
    web.get(url)
    web.find_element("xpath", '//*[@id="ls_username"]').send_keys(username)
    web.find_element("xpath", '//*[@id="ls_password"]').send_keys(password)
    web.find_element("xpath", '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()
    sleep(3)


def get_cookie(num):
    cookies_list = web.get_cookies()
    with open(f"cookies/cookies{num}.txt", "w") as f:
        json.dump(cookies_list, f)


def change_window(window_number, url):
    web.execute_script("window.open('');")
    web.switch_to.window(web.window_handles[window_number])
    web.get(url)

def create_account(url, username, password, email):
    web.get(url)# 連接註冊賬戶域名
    web.find_element("xpath", '//*[@id="shireuser"]').send_keys(username) # 賬戶信息
    web.find_element("xpath", '//*[@id="shirepass"]').send_keys(password)
    web.find_element("xpath", '//*[@id="shirepass2"]').send_keys(password)
    web.find_element("xpath", '//*[@id="shiremail"]').send_keys(email)
    web.find_element("xpath", '//*[@id="registerformsubmit"]/strong').click()
    sleep(3)

def questions_table(qq_num):
    sleep(3)
    web.execute_script('document.querySelectorAll(".question-section")[0].querySelectorAll(".radio-option")[0].querySelector(".radio-custom").click()')
    web.execute_script('document.querySelectorAll(".question-section")[1].querySelectorAll(".radio-option")[0].querySelector(".radio-custom").click()')
    web.execute_script('document.querySelectorAll(".question-section")[3].querySelectorAll(".radio-option")[0].querySelector(".radio-custom").click()')
    web.execute_script('document.querySelectorAll(".question-section")[4].querySelectorAll(".radio-option")[0].querySelector(".radio-custom").click()')
    web.execute_script('document.querySelectorAll(".option-text")[17].click()')
    web.find_element("xpath", '/html/body/app-root/app-questionaire/div/form/div[6]/div/input').click()
    web.find_element("xpath", '/html/body/app-root/app-questionaire/div/form/div[6]/div/input').send_keys(qq_num)
    sleep(0.1)
    web.execute_script('document.querySelector(".submit-btn").click()')

if __name__ == '__main__':
    for list_num in range(len(user_name)):
        print("[INFO] 打開瀏覽器")
        opt = Options()
        opt.add_argument("--headless")
        opt.add_argument("--disable-gpu")
        web = Chrome(options=opt)
        print("[INFO] 創建賬號")
        create_account(url2, user_name[list_num], pass_word[list_num], user_mail[list_num])
        # login_account(url3, user_name[list_num], pass_word[list_num])
        print("[INFO] 切換窗口")
        change_window(1, url4)
        print("[INFO] 填寫問卷")
        questions_table(qq_num)
        print("[INFO] 獲得cookie")
        get_cookie(list_num)
        web.close()
        print("[INFO] 結束")


# user_name_list = [f"UserName4CdC{i}" for i in range(10)]
# print(f"user_name = {user_name_list}")
# pass_word_list = [f"PassWord4CdC{i}" for i in range(10)]
# print(f"pass_word = {pass_word_list}")
# email_list =[f"mail{i}@cdc.com" for i in range(10)]
# print(f"user_mail = {email_list}")
