from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

web = Chrome()

web.get("https://www.autohome.com.cn/beijing/")
# choice1 = web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/section[2]/div[1]/div[2]/div/div[1]/div[1]/label[1]/span[1]/input')
# choice2 = web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/section[2]/div[1]/div[2]/div/div[1]/div[1]/label[2]/span[1]/input')
# print(choice1.get_property('checked'))
# print(choice2.get_property('checked'))

parent = web.find_element(By.XPATH, '//div[@class="ant-radio-group ant-radio-group-outline"]')
choices = parent.find_elements(By.XPATH, './label/span/input')
print(choices)
for choice in choices:
    print(choice.get_property('checked'))
input()