from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://www.youtube.com/watch?v=ayDCnKIhrcw"
url2 = "https://www.google.com.tr/"
a = 0
while a < 10:
    driver.get(url)
    time.sleep(1)
    driver.get(url2)
    a +=1


    # Video izleme bot deneme olayıydı .
    # Çalışıyor :)
    