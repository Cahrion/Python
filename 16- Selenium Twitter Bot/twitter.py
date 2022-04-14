from twitterUserInfo import email, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twit:
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.email = email
        self.password = password
        self.url = 'https://twitter.com/login'
        self.hastag = 'Python'
        self.NextGo = 'https://twitter.com/search?q='
        self.NextNo = '&src=typed_query'
        self.list = []
    def Giriş(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input').send_keys(self.email)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input').send_keys(Keys.ENTER)
        time.sleep(1)
    def Arayış(self):
        self.browser.get(self.NextGo+self.hastag+self.NextNo)
        time.sleep(4)

        last_height = self.browser.execute_script('return document.documentElement.scrollHeight')
        LoupCounter = 0
        s = 1
        foring = self.browser.find_elements_by_xpath('//div[@data-testid="tweet"]/div[2]/div[2]')
        for Fors in foring:
            a = Fors.text.split("\n")            
            self.list.append(f'{s} - {a[0]}')
            s +=1


        while True:
            if LoupCounter < 4:  
                self.browser.execute_script('window.scrollTo(0,document.documentElement.scrollHeight);')
                time.sleep(2)
                new_height = self.browser.execute_script('return document.documentElement.scrollHeight')
                if last_height == new_height:
                    break
                last_height = new_height
                LoupCounter +=1
                foring = self.browser.find_elements_by_xpath('//div[@data-testid="tweet"]/div[2]/div[2]')
                for Fors in foring:
                    a = Fors.text.split("\n")            
                    self.list.append(f'{s} - {a[0]}')
                    s +=1
                time.sleep(2)
            else:
                break

    def Birleştirme(self):
        with open('Twitler.txt', "w", encoding='UTF-8') as file:
            for now in self.list:
                file.write(f'{now} \n')
                


Twittim = Twit(email, password)
#Login
Twittim.Giriş()
#Search
Twittim.Arayış()
Twittim.Birleştirme()