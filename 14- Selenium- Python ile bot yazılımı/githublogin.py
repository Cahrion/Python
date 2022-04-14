from githubUsernfo import username, password
from selenium import webdriver
import time 

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
        time.sleep(1)
        self.browser.get("https://github.com/sadikturan?tab=followers")
    def After(self):
        time.sleep(2)
        ass = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for Yaz in ass:
            self.followers.append(Yaz.find_element_by_css_selector(".link-gray").text)
            
    def Extra(self):
        while True:
            wow = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")
            
            if len(wow) == 1:
                if wow[0].text == "Next":
                    self.After()
                    wow[0].click()
                else:
                    break
            else:
                self.After()
                wow[1].click()
        print(self.followers)
        print(len(self.followers))

github = Github(username, password)
github.signIn()
github.After()
github.Extra()

