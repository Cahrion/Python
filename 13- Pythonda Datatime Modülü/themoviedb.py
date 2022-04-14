# themoviedb.org => film ve dizi arşivi
# themoviedb' nin sundugu apiyi uygulamanızda kullanız'
# anahtar kelimeye göre arama
# en popüler film listesi
# vizyondaki film listesi


import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "api_key=e8a9d5f82d78ca210c8076d648685c12"
        self.page = "&language=en-US&page="
    def Kapı(self, hastag, num):
        response = requests.get(f"{self.api_url}{hastag}{self.api_key}{self.page}{num}")
        return response.json()
    def Kapıs(self, hastags, num):
        response = requests.get(f"{self.api_url}search/keyword?{self.api_key}&query={hastags}&page={num}")
        return response.json()
Movie = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Now-Playing\n3- Search\n4- Exit\nSeçim: ")

    if secim == "4":
        break
    else:   # Website'si kendini korudugu için url'yi alamadım o yüzden kodlar geçersiz görülebilir
            # Key api düzgün seçildiginde doğrulanacaktır.
        if secim == "1":
            c = 1
            while True:
                movies = Movie.Kapı("movie/popular?", c)
                Totalpage = int(movies["total_pages"])
                movies = movies["results"]
                for moviess in movies:
                    print(f'Filim adı: {moviess["title"]}\n-Populerlik: {moviess["popularity"]}')
                print(f"Page: {c}/{Totalpage} Çıkmak için 'q' yazınız")
                Sayfa = input("Geçmek istediginiz sayfa: ")
                if Sayfa == "q":
                    break
                else:
                    if (int(Sayfa) < Totalpage) and int(Sayfa) > 1:
                        c = int(Sayfa)
                    else: 
                        print(f"Lütfen 1-{Totalpage} arasında sayı yazınız.")
                        break
        elif secim == "2":
            w = 1
            while True:
                movies = Movie.Kapı("movie/now_playing?", w)
                movies = movies["results"]
                Totalpage = int(movies["total_pages"])
                for moviess in movies:
                    print(f'Filim adı: {moviess["title"]}\n-Populerlik: {moviess["popularity"]}')
                print(f"Page: {Totalpage}/10 Çıkmak için 'q' yazınız")
                Sayfas = input("Geçmek istediginiz sayfa: ")
                if Sayfas == "q":
                    break
                else:
                    if (int(Sayfas) < Totalpage) and int(Sayfas) > 1:
                        w = int(Sayfas)
                    else: 
                        print(f"Lütfen 1-{Totalpage} arasında sayı yazınız.")
                        break
        elif secim == "3":
            a = input("Aradığınız film: ")
            b = 1
            while True:
                movies = Movie.Kapıs(a, b)
                Totalpage = int(movies["total_pages"])
                movies = movies["results"]
                for moviess in movies:
                    print(f'Filim adı: {moviess["name"]}\n-Numarası: {moviess["id"]}')
                print(f"Page: {b}/{Totalpage} Çıkmak için 'q' yazınız")
                Sayfa = input("Geçmek istediginiz sayfa: ")
                if Sayfa == "q":
                    break
                else:
                    if (int(Sayfa) < Totalpage) and int(Sayfa) > 1:
                        b = int(Sayfa)
                    else: 
                        print(f"Lütfen 1-{Totalpage} arasında sayı yazınız.")
                        break