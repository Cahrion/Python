from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


url = "http://github.com"
driver.get(url)

searchInput = driver.find_element_by_name("q")
# searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div[3]/div/div/form/label/input[1]")
# Daha kolay bir şekilde ulaşmak için chrome özelligi.
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)

searchInput.send_keys(Keys.ENTER)

result = driver.find_elements_by_class_name("v-align-middle") # Başardık anamm
time.sleep(2)
for element in result:
    print(element.text)

result = driver.page_source # Ek olarak bir eklemme yapabilir ve düzeltilebilecek html kodları alabilirsin.

driver.close()