
# x, y, z, = 5, 16, 20

# x, y = y, x

# x += 5          # x = x + 5
# x -= 5          # x = x - 5
# x *= 5          # x = x * 5
# x /= 5          # x = x / 5
# x %= 5          # x = x % 5
# y //= 5         # y = y // 5
# y **= 5         # y = y ** 5 



# print(x,y,z)

values = 1, 2, 3, 4, 5 
print(values)
print(type(values))

x, y, *z = values           # " * "  öne gelen bu işaret liste açıp kapama yapıyor.

print(x, y, z)
print(x, y, z[2])