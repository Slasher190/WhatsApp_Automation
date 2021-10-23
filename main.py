from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from pathlib import Path
p = Path("img.jpg").resolve()
file = str(p)

driver = webdriver.Chrome('./chromedriver')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# target = ['"Sundari"','"Prasoon Mishra"','"Vigyan Gupta"']
# a = ''
with open('namList.txt') as f:
    contents = f.read()
    a=contents
    # print(contents)
tar = list(a.split('\n'))
target = []
for i in range(len(tar)-1):
    target.append(tar[i])
# print(len(p)) 
# Replace the below string with your own message
string = "Sudhi sent 100 Rs !!!"
# file = "./img.jpg"
for i in target:
    x_arg = '//span[contains(@title,' + i + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    input_box.send_keys(string + Keys.ENTER)
    try:

        attach = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@title ='Attach']")))
        attach.click()

        s = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"][@type="file"]')))
        s.send_keys(file)

        send = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
        send.click()

    except Exception as e:
        print(e)
        break    
    time.sleep(1)
