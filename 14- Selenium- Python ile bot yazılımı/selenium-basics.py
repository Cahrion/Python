from selenium import webdriver
import time

driver = webdriver.Chrome()


url = "http://github.com"
driver.get(url)

time.sleep(2) # zamana baglı bir bekleme yapar.

driver.maximize_window() # Ekranı büyütür.
driver.save_screenshot("github.com-homepage.png") # Gittigi yerin ekranını alır.


url = "http://github.com/icabiKrgz"
driver.get(url)

print(driver.title) # Ekrandak title' ı yazdırır

if "icabiKrgz" in driver.title:
    driver.save_screenshot("github-icabiKrgz.png")
time.sleep(2)
driver.back() # En son yaptıgını geri alır.
# driver.forward() # Back yaptıgıysa geri alır - Back'ın tersi.
time.sleep(2)
driver.close()