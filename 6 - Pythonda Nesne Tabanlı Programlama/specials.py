mylist = [1,2,3]
# myString = "My String"

# print(len(mylist))
# print(len(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
    def __str__(self):
        return f"{self.title} the {self.director}"
    
    def __len__(self):
        return self.duration

    def __del__(self):
        print(f"Movie class'ı silindi.")

m = Movie("Film adı","Unutulmaz",120)


# print(mylist)
print(m) # görev bitince bütün dosya silindiginden dolayı silindi mesajı gelir.
# print(len(m))
