# def greeting(name):
#     print(f"Hello {name}")

# print(greeting("ali"))


# sayHello = greeting

# print(sayHello)
# print(greeting)
# print(greeting)
# del greeting
# print(sayHello)

# encapsulation
# def outer(num1):
#     print("outher")
#     def inner_increment(num1):
#         print("inner")
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)
# outer(10)


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):

        if number <= 1:
            return 1
        else:
            return number * inner_factorial(number - 1)
    return inner_factorial(number)
try: 
    print(factorial(-1))
except Exception as ex:
    print(ex)