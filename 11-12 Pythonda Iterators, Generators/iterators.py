liste = [1,2,3,4,5]

# iterator = iter(liste)

# print(next(iterator)) # adım adım yazar
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# aynısını for da yapıyor yani
# print("--")
# aynısını for da yapıyor yani

# for i in liste:
#     print(i)

# For'un yaptıgı ise alttaki
# print("--")
# For'un yaptıgı ise alttaki

# iterator = iter(liste)

# while True:
#     try:
#         print(next(iterator))
#     except Exception:
#         break


class myNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop



    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start+=1
            return x
        else:
            raise StopIteration

list = myNumbers(10,20)


myiter = iter(list)


while True:
    try:
        print(next(myiter))
    except StopIteration:
        break

# for x in list:
#     print(x)


