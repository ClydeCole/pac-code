from time import sleep

from selenium.webdriver import Chrome

web = Chrome()

web.get("https://www.126.com")
# sleep(1)
# switch_account_login_botton = web.find_element("xpath", '//*[@id="lbNormal"]')
# switch_account_login_botton.click()

iframe_div = web.find_element("xpath", './/div[@class="loginUrs"]')
iframe = iframe_div.find_element("xpath", 'iframe')


web.switch_to.frame(iframe)
input()
