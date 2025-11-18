from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client

web = Chrome()
web.get("https://www.chaojiying.com/user/login/")

png = web.find_element("xpath", '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('ClydeCole682', 'QAZ527452874', '974150')
result = chaojiying.PostPic(png, 1004)

print(result)
v_code = result["pic_str"]

web.find_element("xpath", '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("ClydeCole682")
web.find_element("xpath", '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("QAZ527452874")
web.find_element("xpath", '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(v_code)
web.find_element("xpath", '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

input()