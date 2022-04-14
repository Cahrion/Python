# value types => string, number
x = 10
y = 30

x = y 

y = 15
                    # Bir degişken eşitlikten dolayı diğeri degişirse o degişmez.
# print(x,y)


#reference types => list
a = ["apple","banana"]
b = ["apple","banana"]

a = b
b[0] = "grape"
print(a,b)
                    # Bir list aynı listenin elemanları ve eşitlik sağlanırsa ikiside degişir.
                    # Adreslere gittiklerinden dolayı hepsi birlikte degişir.
    
    

    # value type = verinin kendisiyle
    # reference types = verinin adresiyle ilgilenicez.
