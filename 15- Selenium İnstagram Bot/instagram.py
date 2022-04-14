from instagramUserInfo import email, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.instagram.com/accounts/login"
url2 = 'https://www.instagram.com/icabi.krgz'
url3 = 'https://www.instagram.com/'

class patates:
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.password = password
        self.email = email
        self.list = ['therock','selenagomez','icabi.krgz']
    def Baslat(self):
        self.browser.get(url)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.email)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(2.5)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(2)
    def Follower(self):
        self.browser.get(url2)
        Takip = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        time.sleep(2)
        
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(1)
        Dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(Dialog.find_elements_by_css_selector("li"))

        print(f"First count: {followerCount}/{Takip.text}")
        Takip = Takip.text.split(",")
        if len(Takip) == 2:
            Nere = int(Takip[0])*1000 +int(Takip[1])
        else:
            Nere = int(Takip[0])
        
        action = webdriver.ActionChains(self.browser)

        while True:
            Dialog.click()
            followerCount = len(Dialog.find_elements_by_css_selector("li"))
            if int(followerCount) >= Nere-5:
                break
            else:
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.2)
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                print(followerCount)

        Tekrar = Dialog.find_elements_by_tag_name('li')
        
        for Tek in Tekrar:
            Ad = Tek.find_element_by_css_selector(".FPmhX.notranslate").text
            Adres = Tek.find_element_by_css_selector(".FPmhX.notranslate").get_attribute("href")
            with open("Follower.txt", "a", encoding='utf-8') as file:
                file.write(f'{Ad.ljust(60)} | {Adres}\n')
            
            print(f'{Ad.ljust(60)} | {Adres}')
    def Takip(self):
        for oynat in self.list:
            self.browser.get(url3 + oynat)
            followButton = self.browser.find_element_by_tag_name("button")
            
            if (followButton.text == ""):
                print("Çalışması için hesabınızı gizliden çıkarmanız gerekmektedir.")
            elif (followButton.text == "Message"):
                print("Saden bu hesabı takip etmektesiniz.")
            else:
                followButton.click()
    def UnTakip(self):
        for oynat in self.list:
            self.browser.get(url3 + oynat)
            followButton = self.browser.find_element_by_tag_name("button")
            if followButton.text == 'Message':
                self.browser.find_elements_by_tag_name("button")[1].click()
                time.sleep(1)
                self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                time.sleep(1)
            else:
                print("Takip etmiyorsunuz.")



patato = patates(email, password)

patato.Baslat()
# patato.Takip()
# patato.UnTakip()
patato.Follower()