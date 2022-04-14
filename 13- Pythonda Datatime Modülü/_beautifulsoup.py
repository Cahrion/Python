html_doc = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Sitesi</title>
</head>
<body>
    <h1>
        Programlama

    </h1>
    <div class="grup1">
        <h2>Selam canlar seviliyorsunuz. </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 1</li>
            <li>Menü 1</li>
            <li>Menü 1</li>
        </ul>
    </div>
    <h1> Monster

    </h1>
    <div class="grup3">
        <h2>Selam canlar seviliyorsunuz. </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 1</li>
            <li>Menü 1</li>
            <li>Menü 1</li>
        </ul>
    </div>
    <h1> Mödüller

    </h1>
    <div class="grup2">
        <h2>Selam canlar seviliyorsunuz. </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 1</li>
            <li>Menü 1</li>
            <li>Menü 1</li>
        </ul>
    </div>
    <img src="IMG-20200205-WA0559.jpg" alt="">
    <a class="sister" href="https://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="https://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="https://example3.com/elsie" id="link1">Elsie</a>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify() # Düzenler.
result = soup.title
result = soup.head
result = soup.body


result = soup.title.name # Title ismi gelri.
result = soup.title.string # iç bilgiyi verir.


result = soup.h1.name
result = soup.h1.string 

result = soup.find_all("h1")

result = soup.div
result = soup.find_all("div")[1] # İkinci 'div' etiketini bulduk
result = soup.find_all("div")[1].ul.li # Div etiketi içindeki ul' metodunu sonra ise li' metodunu bulduk
result = soup.find_all("div")[1].ul.find_all("li") # Hepsinin içindeki 'li' etiketini bulduk

result = soup.div.findChildren()

result = soup.div.findNextSiblings()[1]

result = soup.prettify()
result = soup.find_all("a")
for link in result:
    print(link.get("href"))

