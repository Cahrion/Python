import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
soup = BeautifulSoup("")
response = requests.get(url).content
soup = BeautifulSoup(response, "html.parser")

soup = soup.find("tbody",{'class':'lister-list'}).find_all("tr")
a = 1
print(" Top 250 ".center(100, "-"))
for tr in soup:
    trs = tr.find("td").findNextSiblings()[0]
    rating = tr.find("td").findNextSiblings()[1]
    Year = trs.span.text
    ws = trs.a.get('title').split("(dir.)")
    print(f"∗{a}∗ {trs.a.string} -{Year}- filminin yazarı: {ws[0]} ✰ {rating.strong.text}")
    a +=1
print(" Top 250 ".center(100, "-"))