from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import loginInfo
import os

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--incognito")
chromedriver_path = './chromedriver'

open_file = open("usersList.txt", "w")

browser = webdriver.Chrome(
    executable_path=chromedriver_path,
    options=options)  #Start Browserrowser.get("https://www.instagram.com/")

time.sleep(3)  # Waiting 3 seconds after we open the page.

#IG Login -->

username = browser.find_element_by_name("username")
username.send_keys(loginInfo.username)

password = browser.find_element_by_name("password")
password.send_keys(loginInfo.password)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
time.sleep(6)

browser.get(
    "https://www.instagram.com/accounts/access_tool/current_follow_requests")

while True:
    try:
        # vm_button = browser.find_element_by_xpath("//button[@type='button']")
        button = browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/article/main/button")
        button.click()
        time.sleep(2)
    except NoSuchElementException:
        break

req_source = browser.find_elements_by_xpath("//div[@class='-utLf']")

count = 0

for x in req_source:
    open_file.write(x.text + "\n")
    count += 1
open_file.close()

print(
    "Got " + str(count) +
    " users you have sent follow request in \"usersList.txt\" file, now exiting browser..."
)
browser.quit()
os.system('python cancel_request.py')
