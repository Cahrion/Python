import requests
import json





class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "9c2066c93c3f816d2ea59a3e8d419e69b71ec623"
    def getUser(self, username):
        response = requests.get(self.api_url+"/users/" + username)
        response = json.loads(response.text)
        return f"Ad: {response['login']}\nNumarası: {response['id']}"

    def getRepositories(self,username):
        responsed = requests.get(self.api_url+"/users/"+username +"/repos")
        responsed = json.loads(responsed.text)
        return responsed

    def createRepository(self, name):
        response = requests.post(self.api_url+"/user/repos?access_token=" + self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
Git = Github()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ")
    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Bulmak istediginiz kullanıcı: ")
            print(Git.getUser(username))
        elif secim == "2":
            username = input("Bulmak istediginiz kullanıcı: ")
            w = Git.getRepositories(username)
            for kor in w:
                print(f"Adı: {kor['name']}\nKoruma: {kor['private']}")

        elif secim == "3":
            names = input("repository name: ")
            resul = Git.createRepository(names)
            print(resul)
        else:
            print("Yanlış bir seçim yaptınız.")
