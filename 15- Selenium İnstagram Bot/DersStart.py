from selenium import webdriver
import time
url = "https://1milyonistihdam.hmb.gov.tr/ozgecmis/login?type=btk"
urls = 'https://www.btkakademi.gov.tr/portal/course/deliver/s-f-rdan-ileri-seviye-python-programlama-5877#!/play'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
username = "54838068282"
password = "Matter456"

soup = driver.find_element_by_xpath('//*[@id="identification"]')
soup.send_keys(username)
passw = driver.find_element_by_xpath('//*[@id="password"]')
passw.send_keys(password)
driver.find_element_by_xpath('//*[@id="loginform"]/button').click()
time.sleep(2)
driver.get(urls)
