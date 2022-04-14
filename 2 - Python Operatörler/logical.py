x = 7

hak = 5
devam = str(input("Devam etmek istiyor musunuz? "))

result = 5 < x < 10
# and

result = (x > 5) and (x < 10) 

result = (hak > 0) and (devam == "e")
print(result)
                # True, True = > True
                # True, false = > false


# or

bo = (x > 0) or (x % 2 == 0)
print(bo)
                # True, True => True
                # True, False => True
                # False, False => False

# not

no = not(x > 0)

print(no)
# x, 5-10 arasında olan bir çift sayı mı ?

wit = ((x > 5) and (x < 10)) and (x % 2 == 0)

print(wit)

