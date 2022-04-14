# def cube():


#     for i in range(5):
#         yield i ** 3 # iterlator yapar

# for i in cube():
#     print(i)


# generator = cube()

# iterator = iter(generator)
# while True:
#     try: 
#         print(next(iterator))
#     except Exception:
#         break

liste = (i**3 for i in range(5))
for z in liste:
    print(z)