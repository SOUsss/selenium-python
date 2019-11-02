import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()
elem = browser.find_element(BY.TAG,"label")
elem.send_keys("RHFU")
nnn= browser.find_element(BY.NAME,"last_name")
nnn.send_keys("LLLL")
ccc= browser.find_element(BY.CLASS_NAME,"form-control.city")
ccc.send_keys("CCCC")
kkk= browser.find_element(BY.ID,"country")
kkk.send_keys("KKKK")
bbb= browser.find_element(BY.CLASS_NAME,"submit.btn")
bbb.click()



browser.quit()

