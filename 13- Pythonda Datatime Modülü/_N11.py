from bs4 import BeautifulSoup
import requests


url_n11 = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
sayfa = "?pg="
response = requests.get(url_n11).content
soup = BeautifulSoup(response, "html.parser")
soup = soup.find("section").find("div",{'class':'listView'}).ul.find_all("li",{'class':'column'})
print(" Fiyat ".center(100, "-"))
a = 1
for List in soup:
    Listing = List.find("div").find("div", {'class':'pro'}).h3.text.strip()
    Fiyat = List.find('div').find("div", {'class':'proDetail'}).find("a",{'class':'newPrice'}).ins.text.strip().split("\n")[0]
    if a > 9:
        print(f'{a} - {Listing.ljust(70)} |-{Fiyat}TL')
    else:
        print(f'{a}  - {Listing.ljust(70)} |-{Fiyat}TL')
    a +=1
print(" Fiyat ".center(100, "-"))
while True:
    s = int(input("Diğer sayfa: "))
    print(" Fiyat ".center(100, "-"))
    responses = requests.get(f"{url_n11}{sayfa}{s}").content
    soups = BeautifulSoup(responses, "html.parser")
    soups = soups.find("section").find("div",{'class':'listView'}).ul.find_all("li",{'class':'column'})

    for List in soups:
        Listing = List.find("div").find("div", {'class':'pro'}).h3.text.strip()
        Fiyat = List.find('div').find("div", {'class':'proDetail'}).find("a",{'class':'newPrice'}).ins.text.strip().split("\n")[0]
        print(f'✰- {Listing.ljust(70)} |-{Fiyat}TL')

    print(" Fiyat ".center(100, "-"))