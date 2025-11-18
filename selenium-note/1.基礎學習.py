from selenium.webdriver import Chrome

web = Chrome()
web.get("https://www.bilibili.com")
print(web.title)
web.quit()


# import requests
# import re
#
# response = requests.get('https://www.bilibili.com', headers={'user-agent': 'Mozilla/5.0'})
# response.encoding = 'utf-8'
# title = re.findall(r'<title>(.*?)</title>', response.text)
# print(title)